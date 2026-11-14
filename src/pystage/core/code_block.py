import ast
import inspect
import textwrap
import types

from pystage.core.i18n import tr

from pystage.l10n.api import get_core_function_from_instance

# Functions that need to be yielded for screen refresh
yield_funcs = [
    "control_wait",
    # Stop needs to yield so that the next command is not executed
    "control_stop_all",
    "control_stop_this",
    "control_stop_other",
    "sound_playuntildone",
    "motion_glidesecstoxy",
    "motion_glideto_random",
    "motion_glideto_sprite",
    "motion_glideto_pointer",
    "sensing_askandwait",
    "event_broadcastandwait",
    "looks_switchbackdroptoandwait",
    "control_delete_this_clone",
    "looks_sayforsecs",
    "looks_thinkforsecs",
]


class CodeManager():
    def __init__(self, owner):
        # name: code_block
        self.code_blocks: dict[str, CodeBlock] = {}
        # pygame.K_?: [name, ...]
        self.key_pressed_blocks = {}
        # message: [name, ...]
        self.broadcast_blocks = {}
        self.clicked_blocks = []
        self.cloned_blocks = []
        # Fired for every key
        self.any_key_blocks = []
        # backdrop name (lower case): [code_block, ...]
        self.backdrop_blocks = {}
        # [[value, code_block, armed], ...]
        self.timer_blocks = []
        # Name of the code block currently executed.
        # This way, state about the current execustion
        # can be stored safely where it belongs
        self.current_block: CodeBlock = None
        self.owner = owner

    def stop_running_blocks(self):
        for name in self.code_blocks:
            self.code_blocks[name].stop()

    def process_key_pressed(self, key):
        # key is a pygame constant, e.g. pygame.K_a
        # This hat block is special as it only fires again when the code block has ended. 
        # All other hat block methods stop the current execution and restart the block.
        for name in self.key_pressed_blocks.get(key, []):
            self.code_blocks[name].start_if_not_running()
        for block in self.any_key_blocks:
            block.start_if_not_running()

    def process_click(self):
        for block in self.clicked_blocks:
            block.start_or_restart()

    def process_broadcast(self, message):
        started = []
        for name in self.broadcast_blocks.get(_message_key(message), []):
            self.code_blocks[name].start_or_restart()
            started.append(self.code_blocks[name])
        return started

    def process_backdrop(self, backdrop):
        started = []
        for block in self.backdrop_blocks.get(str(backdrop).strip().lower(), []):
            block.start_or_restart()
            started.append(block)
        return started

    def process_timer(self, timer):
        # Fires once when the timer gets greater than the value. It can fire
        # again as soon as the timer was reset.
        for entry in self.timer_blocks:
            value, block, armed = entry
            if timer > value:
                if armed:
                    entry[2] = False
                    block.start_or_restart()
            else:
                entry[2] = True

    def register_code_block(self, generator_function, name="", no_refresh=False):
        new_block = CodeBlock(self.owner, generator_function, name, no_refresh=no_refresh)
        self.code_blocks[new_block.name] = new_block
        return new_block

    def _update(self, dt):
        for name in self.code_blocks:
            self.current_block = self.code_blocks[name]
            self.code_blocks[name].update(dt)

    def clone(self, owner):
        clone = CodeManager(owner)
        blocks = {}
        for name in self.code_blocks:
            code_block = self.code_blocks[name]
            cloned_block = CodeBlock(owner, code_block.generator_function, "clone", code_block.no_refresh, transform=False)
            clone.code_blocks[cloned_block.name] = cloned_block
            blocks[name] = cloned_block
        # All events of the original are bound for the clone as well
        clone.key_pressed_blocks = {k: [blocks[n].name for n in v] for k, v in self.key_pressed_blocks.items()}
        clone.broadcast_blocks = {k: [blocks[n].name for n in v] for k, v in self.broadcast_blocks.items()}
        by_block = {block: blocks[name] for name, block in self.code_blocks.items()}
        clone.clicked_blocks = [by_block[b] for b in self.clicked_blocks]
        clone.cloned_blocks = [by_block[b] for b in self.cloned_blocks]
        clone.any_key_blocks = [by_block[b] for b in self.any_key_blocks]
        clone.backdrop_blocks = {k: [by_block[b] for b in v] for k, v in self.backdrop_blocks.items()}
        clone.timer_blocks = [[value, by_block[b], armed] for value, b, armed in self.timer_blocks]
        return clone


def _message_key(message):
    # Messages are not case sensitive in Scratch
    return str(message).strip().lower()

class CodeBlock():
    '''
    The CodeBlock encapsulates a generator and manages its state.

    
    '''
    last_id = -1

    def __init__(self, sprite_or_stage, generator_function, name="", no_refresh=False, transform=True):
        '''
        Parameters
        ----------
        sprite_or_stage :
            The sprite or stage instance this code block is associated with
        generator_function : function
            The function containing the code to be executed. It can be a generator 
            function or a normal function which will be turned into a generator function
            if no_refresh is set to False (default)
        name : str, optional
            A name postfix used to distinguish this code block from other code blocks
            using the same function.
        no_refresh : bool, optional
            If set to true, the function must not be a generator function and will also
            not turned into one. This means that the screen will not be refreshed until
            the function returns.

        Raises
        ------
        ValueError
            If the function does not get a single parameter (for the reference to 
            the sprite or stage) or if a generator function is supplied with no_refresh 
            set to True. 
        '''
        if len(inspect.signature(generator_function).parameters) == 0:
            self.inject_instance = False
        elif len(inspect.signature(generator_function).parameters) == 1:
            self.inject_instance = True
        else:
            raise ValueError(tr("block_parameters", name=generator_function.__name__))

        self.sprite_or_stage = sprite_or_stage
        if name != "" and name != None:
            name = f"-{name}"
        CodeBlock.last_id += 1
        # The name of a code block is unique with a global id.
        # A custom name may be provided to distinguish blocks
        # that use the same generator function.
        # This is not possible in Scratch (you only can copy blocks), 
        # but could be allowed here.
        # TODO: Discuss, if we should completely prohibit the 
        # reuse of generators, it could make things easier.
        self.name = f"{generator_function.__name__}{name}-{CodeBlock.last_id}"
        # A copy of the generator_function used for restarts (e.g. when bound to events)
        self.generator_function = generator_function
        # The current state of a generator after it is started
        self.generator = None
        self.is_function = False
        self.no_refresh = no_refresh
        if inspect.isgeneratorfunction(generator_function):
            if no_refresh:
                raise ValueError(tr("block_no_refresh", name=generator_function.__name__))
        else:
            if no_refresh:
                # We support also plain functions, i.e. without yield
                self.is_function = True
            elif transform:
                self.generator_function = self.add_yields(generator_function)

        # The time until the next step is executed
        self.wait_time = 0
        self.add_to_wait_time = 0
        self.gliding = False
        self.gliding_seconds = 0
        self.gliding_start_position = (0, 0)
        self.gliding_end_position = (0, 0)

        self.saying = False
        # Flag indicating if the block is currently running
        self.running = False
        # Ask mode (waiting for user input)
        self.asking = False
        # Code blocks that have to finish before this block continues
        self.waiting_for = []

    def ask(self, question):
        # Go into "ask" mode
        self.asking = True
        # Queue the question in the central input manager
        self.sprite_or_stage.stage.input_manager.queue(question, self)


    def start_if_not_running(self):
        '''
        Start the code block. If the block is already started,
        this method does nothing.
        '''
        if self.running:
            return
        self.start_or_restart()

    def start_or_restart(self):
        '''
        (Re-)start the code block. If the block is already started,
        the current execution will not continue.
        '''
        self.running = True
        self.wait_time = 0
        self.add_to_wait_time = 0
        self.waiting_for = []
        self.gliding = False
        self.saying = False
        if not self.is_function:
            target = self.sprite_or_stage
            if self.sprite_or_stage.facade:
                target = self.sprite_or_stage.facade
            if self.inject_instance:
                self.generator = self.generator_function(target)
            else:
                self.generator = self.generator_function()

    def stop(self):
        """
        If there is other behaviors need to be stopped, add them here.
        """
        if self.asking:
            self.sprite_or_stage.stage.input_manager.cancel(self)
        self.running = False
        self.asking = False
        self.saying = False
        self.gliding = False

    def update(self, dt):
        '''
        Check if it is time for the next step and execute it.
        '''
        if not self.running:
            return
        # Do nothing while waiting for an answer.
        if self.asking:
            return
        # ... or for other code blocks (e.g. broadcast and wait)
        if self.waiting_for:
            if any(block.running for block in self.waiting_for):
                return
            self.waiting_for = []
        self.wait_time -= dt
        if self.wait_time <= 0:
            if self.gliding:
                self.sprite_or_stage.motion_gotoxy(*self.gliding_end_position)
                self.gliding = False
            if self.saying:
                self.sprite_or_stage.bubble_manager.kill()
                self.saying = False
            if self.is_function:
                self.running = False
                if self.inject_instance:
                    self.generator_function(self.sprite_or_stage.facade or self.sprite_or_stage)
                else:
                    self.generator_function()
                return
            else:
                try:
                    result = next(self.generator)
                    self.wait_time = 0
                    if isinstance(result, float) or isinstance(result, int):
                        self.wait_time = result
                    if self.add_to_wait_time > 0:
                        self.wait_time += self.add_to_wait_time
                        self.add_to_wait_time = 0
                except StopIteration:
                    self.running = False
        elif self.gliding:
            self.sprite_or_stage.motion_setx(
                self.gliding_end_position[0] - (self.gliding_end_position[0] - self.gliding_start_position[0]) * (
                            self.wait_time / self.gliding_seconds))
            self.sprite_or_stage.motion_sety(
                self.gliding_end_position[1] - (self.gliding_end_position[1] - self.gliding_start_position[1]) * (
                            self.wait_time / self.gliding_seconds))

    def add_yields(self, function):
        '''
        This function does the black magic and adds yields to the code so that
        the screen can update. This creates a generator function.

        Parameters
        ----------
        function : The function to be transformed to a generator function.
        '''
        return add_yields(function, self.sprite_or_stage.facade)

    def __str__(self):
        return f"<CodeBlock {self.name} - {self.running}>"
    
    def __repr__(self):
        return str(self)


def no_refresh(function):
    '''
    Decorator for helper functions that must run in one go,
    like custom blocks with "run without screen refresh" in Scratch.

    Without it, a helper function called from a code block behaves like the
    code block itself: The screen is refreshed after each loop iteration
    and blocks like wait work as expected.
    '''
    function.no_refresh = True
    return function


# Name of the helper that is injected into the module of the user code.
CALL_HELPER = "__pystage_call__"

# function: generator function
_transformed = {}


def _call(function, *args, **kwargs):
    '''
    Runtime helper for calls of plain functions in code blocks.

    Functions from the same file as the code block are treated like custom
    blocks in Scratch, i.e. they get yields as well and are executed
    step by step. Everything else is simply called.
    '''
    generator_function = _as_generator_function(function)
    if generator_function is None:
        function(*args, **kwargs)
    else:
        yield from generator_function(*args, **kwargs)


def _as_generator_function(function):
    if function in _transformed:
        return _transformed[function]
    result = None
    if (isinstance(function, types.FunctionType)
            and not getattr(function, "no_refresh", False)
            and CALL_HELPER in function.__globals__
            and function.__closure__ is None):
        if inspect.isgeneratorfunction(function):
            result = function
        else:
            try:
                result = add_yields(function)
            except (OSError, TypeError, SyntaxError, IndexError):
                # No source code available, call it normally.
                result = None
    _transformed[function] = result
    return result


# module name: [facade, ...], to resolve translated function names in helpers
_facades = {}


def _takes_time(name, facades):
    '''
    True, if the method with this name is a block after which
    the code block has to yield, see yield_funcs.
    '''
    for facade in facades:
        if get_core_function_from_instance(name, facade) in yield_funcs:
            return True
    return False


def _index_ast(func_ast):
    '''
    Helper function to (re-)generate for each node that is in
    a body or orelse field its parent, the field and its position
    in the field.
    '''
    for node in ast.walk(func_ast):
        for field in ["body", "orelse", "finalbody"]:
            children = getattr(node, field, None)
            if isinstance(children, list):
                for index, child in enumerate(children):
                    child.parent = node
                    child.index = index
                    child.isin = field


def _yield():
    return ast.Expr(value=ast.Yield(value=ast.Constant(value=0)))


def add_yields(function, facade=None):
    '''
    Transforms a function to a generator function with the same behavior
    that yields

    - at the end of each loop iteration,
    - after each call of a block that takes time (see yield_funcs),
    - within functions from the same file that are called as statement.

    Parameters
    ----------
    function : The function to be transformed to a generator function.
    facade : The sprite or stage of the translated API, None for core.
    '''
    module = function.__globals__.get("__name__")
    facades = _facades.setdefault(module, [])
    if not any(type(f) is type(facade) for f in facades):
        facades.append(facade)

    func_ast = ast.parse(textwrap.dedent(inspect.getsource(function)))
    # Keep the line numbers of the original file for error messages
    ast.increment_lineno(func_ast, function.__code__.co_firstlineno - 1)
    func_def = func_ast.body[0]
    if not isinstance(func_def, ast.FunctionDef):
        raise TypeError(tr("block_not_def", name=function.__name__))
    # Decorators (e.g. no_refresh) must not be applied a second time.
    func_def.decorator_list = []

    # yield at the end of the function
    func_def.body.append(_yield())

    _index_ast(func_ast)

    # Nested function definitions and classes are left alone.
    def walk(node):
        yield node
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
                continue
            yield from walk(child)

    nodes = [func_def] + [n for child in ast.iter_child_nodes(func_def) for n in walk(child)]
    after = []
    for node in nodes:
        # yield at the end of for and while iterations
        if isinstance(node, (ast.For, ast.While)):
            node.body.append(_yield())

        if not (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and hasattr(node, "parent")):
            continue
        call = node.value
        if isinstance(call.func, ast.Attribute):
            # yield after certain calls defined in yield_funcs
            if _takes_time(call.func.attr, facades):
                after.append(node)
        elif isinstance(call.func, ast.Name):
            # Functions called as statement could be "custom blocks"
            node.value = ast.YieldFrom(value=ast.Call(
                func=ast.Name(id=CALL_HELPER, ctx=ast.Load()),
                args=[call.func] + call.args,
                keywords=call.keywords))

    for node in after:
        # Positions change with each insert
        _index_ast(func_ast)
        getattr(node.parent, node.isin).insert(node.index + 1, _yield())

    ast.fix_missing_locations(func_ast)
    # print(ast.unparse(func_ast)) # outputs the transformed code
    # The code is executed in the module of the function so that global
    # variables are shared. The new function itself only lives in namespace.
    function.__globals__[CALL_HELPER] = _call
    namespace = {}
    filename = inspect.getsourcefile(function) or "<string>"
    code = compile(func_ast, filename, mode="exec")
    exec(code, function.__globals__, namespace)
    generator_function = namespace[function.__name__]
    generator_function.__defaults__ = function.__defaults__
    generator_function.__kwdefaults__ = function.__kwdefaults__
    return generator_function
