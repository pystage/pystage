import ast
import inspect

from pystage.l10n.api import get_core_function_from_instance

# Functions that need to be yielded for screen refresh
yield_funcs = [
    "control_wait",
    "sound_playuntildone",
    "motion_glidesecstoxy",
    "motion_glideto_random",
    "motion_glideto_sprite",
    "motion_glideto_pointer",
    "sensing_askandwait",
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
        # Name of the code block currently executed.
        # This way, state about the current execustion
        # can be stored safely where it belongs
        self.current_block: CodeBlock = None
        self.running_blocks: list[CodeBlock] = []
        self.owner = owner

    def stop_running_blocks(self):
        for block in self.running_blocks:
            block.stop()
        self.running_blocks = []

    def process_key_pressed(self, key):
        # key is a pygame constant, e.g. pygame.K_a
        # This hat block is special as it only fires again when the code block has ended. 
        # All other hat block methods stop the current execution and restart the block.
        if key in self.key_pressed_blocks:
            for name in self.key_pressed_blocks[key]:
                self.code_blocks[name].start_if_not_running()

    def process_click(self):
        for block in self.clicked_blocks:
            block.start_or_restart()

    def process_broadcast(self, message):
        if message in self.broadcast_blocks:
            for name in self.broadcast_blocks[message]:
                self.code_blocks[name].start_or_restart()

    def register_code_block(self, generator_function, name="", no_refresh=False):
        new_block = CodeBlock(self.owner, generator_function, name, no_refresh=no_refresh)
        self.code_blocks[new_block.name] = new_block
        print(f"New code block registered: {new_block.name}")
        return new_block

    def _update(self, dt):
        for name in self.code_blocks:
            self.current_block = self.code_blocks[name]
            self.code_blocks[name].update(dt)


class CodeBlock():
    '''
    The CodeBlock encapsulates a generator and manages its state.

    
    '''
    last_id = -1

    def __init__(self, sprite_or_stage, generator_function, name="", no_refresh=False):
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
            raise ValueError(
                f"Your code block '{generator_function.__name__}' needs zero or one parameter. The parameter is usually called self.")

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
                raise ValueError(
                    f"Your code block '{generator_function.__name__}' is set to no refresh. In this case, yield must not be used.")
        else:
            if no_refresh:
                # We support also plain functions, i.e. without yield
                self.is_function = True
            else:
                self.generator_function = self.add_yields(generator_function)

        # The time until the next step is executed
        self.wait_time = 0
        self.add_to_wait_time = 0
        self.gliding = False
        self.gliding_seconds = 0
        self.gliding_start_position = (0, 0)
        self.gliding_end_position = (0, 0)
        # Flag indicating if the block is currently running
        self.running = False
        # Ask mode (waiting for user input)
        self.asking = False

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
        self.sprite_or_stage.code_manager.running_blocks.append(self)
        self.running = True
        self.wait_time = 0
        if not self.is_function:
            target = self.sprite_or_stage
            if self.sprite_or_stage.facade:
                target = self.sprite_or_stage.facade
            if self.inject_instance:
                self.generator = self.generator_function(target)
            else:
                self.generator = self.generator_function()
        print(f"Start of {self.name} triggered.")

    def stop(self):
        """
        If there is other behaviors need to be stopped, add them here.
        """
        self.running = False
        self.asking = False
        self.saying = False
        if type(self.sprite_or_stage).__name__ == "CoreSprite":
            self.sprite_or_stage.bubble_manager.kill()
        if type(self.sprite_or_stage).__name__ == "CoreStage":
            self.sprite_or_stage.input_manager.cancel_asking()

    def update(self, dt):
        '''
        Check if it is time for the next step and execute it.
        '''
        if not self.running:
            return
        # Do nothing while waiting for an answer.
        if self.asking:
            return
        self.wait_time -= dt
        if self.wait_time < 0:
            if self.gliding:
                self.x, self.y = self.gliding_end_position
                self.gliding = False
            if self.is_function:
                target = self.sprite_or_stage
                if self.sprite_or_stage.facade:
                    target = self.sprite_or_stage.facade
                self.generator = self.generator_function(target)
                print(f"CodeBlock {self.name} has finished.")
                self.running = False
                self.sprite_or_stage.code_manager.running_blocks.remove(self)
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
                    print(f"CodeBlock {self.name} has finished.")
                    self.running = False
                    self.sprite_or_stage.code_manager.running_blocks.remove(self)
        elif self.gliding:
            self.sprite_or_stage.motion_setx(
                self.gliding_end_position[0] - (self.gliding_end_position[0] - self.gliding_start_position[0]) * (
                            self.wait_time / self.gliding_seconds))
            self.sprite_or_stage.motion_sety(
                self.gliding_end_position[1] - (self.gliding_end_position[1] - self.gliding_start_position[1]) * (
                            self.wait_time / self.gliding_seconds))

    def index_ast(self, func_ast):
        '''
        Helper function to (re-)generate for each node that is in
        a body or orelse field its parent, the field and its position 
        in the field.

        Parameters
        ----------
        func_ast : ast.AST
            The AST to be indexed.
        '''

        for node in ast.walk(func_ast):
            for field in ["body", "orelse"]:
                if hasattr(node, field):
                    for index, child in enumerate(getattr(node, field)):
                        child.parent = node
                        child.index = index
                        child.isin = field

    def add_yields(self, function):
        '''
        This function does the black magic and adds yields to the code so that
        the screen can update. This creates a generator function.

        Parameters
        ----------
        function : The function to be transformed to a generator function.
        '''
        func_ast = ast.parse(inspect.getsource(function))

        # yield at the end of the function
        func_ast.body[0].body.append(ast.Expr(value=ast.Yield(value=ast.Constant(value=0))))

        self.index_ast(func_ast)

        for node in ast.walk(func_ast):

            # yield at the end of for and while iterations
            if isinstance(node, ast.For):
                node.body.append(ast.Expr(value=ast.Yield(value=ast.Constant(value=0))))
            if isinstance(node, ast.While):
                node.body.append(ast.Expr(value=ast.Yield(value=ast.Constant(value=0))))

            # yield after certain calls defined in CodeBlock.yield_funcs
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and isinstance(node.value.func,
                                                                                              ast.Attribute):
                corefunc = get_core_function_from_instance(node.value.func.attr, self.sprite_or_stage.facade)
                if corefunc in yield_funcs:
                    getattr(node.parent, node.isin).insert(node.index + 1,
                                                           ast.Expr(value=ast.Yield(value=ast.Constant(value=0))))
                    # We need to reindex so that further yields get the right position
                    self.index_ast(func_ast)

        ast.fix_missing_locations(func_ast)
        # print(ast.unparse(func_ast)) # outputs the transformed code
        namespace = {}
        namespace.update(function.__globals__)
        code = compile(func_ast, "<string>", mode="exec")
        exec(code, namespace)
        return namespace[function.__name__]
    
    def __str__(self):
        return f"<CodeBlock {self.name} - {self.running}>"
    
    def __repr__(self):
        return str(self)
