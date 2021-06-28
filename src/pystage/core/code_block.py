import inspect
import ast
import importlib

class CodeManager():
    def __init__(self, owner):
        # name: code_block
        self.code_blocks = {}
        # pygame.K_?: [name, ...]
        self.key_pressed_blocks = {}
        # Name of the code block currently executed.
        # This way, state about the current execustion
        # can be stored safely where it belongs
        self.current_block : CodeBlock = None
        self.owner = owner


    def process_key_pressed(self, key):
        # key is a pygame constant, e.g. pygame.K_a
        # This hat block is special as it only fires again when the code block has ended. 
        # All other hat block methods stop the current execution and restart the block.
        if key in self.key_pressed_blocks:
            for name in self.key_pressed_blocks[key]:
                self.code_blocks[name].start_if_not_running()


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
        if len(inspect.signature(generator_function).parameters)!=1:
            raise ValueError(f"Your code block '{generator_function.__name__}' needs one parameter, usually called self.")

        self.sprite_or_stage = sprite_or_stage
        if name!="" and name!=None:
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
                raise ValueError(f"Your code block '{generator_function.__name__}' is set to no refresh. In this case, yield must not be used.")
        else:
            if no_refresh:
                # We support also plain functions, i.e. without yield
                self.is_function = True
            else:
                self.generator_function = add_yields(generator_function)

        # The time until the next step is executed
        self.wait_time = 0
        self.add_to_wait_time = 0
        # Flag indicating if the block is currently running
        self.running = False


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
        if not self.is_function:
            target = self.sprite_or_stage
            if self.sprite_or_stage.facade:
                target = self.sprite_or_stage.facade
            self.generator = self.generator_function(target)
        print(f"Start of {self.name} triggered.")


    def update(self, dt):
        '''
        Check if it is time for the next step and execute it.
        '''
        if not self.running:
            return
        self.wait_time -= dt
        if self.wait_time < 0:
            if self.is_function:
                target = self.sprite_or_stage
                if self.sprite_or_stage.facade:
                    target = self.sprite_or_stage.facade
                self.generator = self.generator_function(target)
                print(f"CodeBlock {self.name} has finished.")
                self.running = False
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


# Helper functions

yield_funcs = ["control_wait", "sound_playuntildone"]
# de
yield_funcs += ["warte", "sound_playuntildone"]


def index_ast(func_ast):
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


def add_yields(function):
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

    index_ast(func_ast)

    for node in ast.walk(func_ast):
        
        # yield at the end of for and while iterations
        if isinstance(node, ast.For):
            node.body.append(ast.Expr(value=ast.Yield(value=ast.Constant(value=0))))
        if isinstance(node, ast.While):
            node.body.append(ast.Expr(value=ast.Yield(value=ast.Constant(value=0))))

        # yield after certain calls defined in CodeBlock.yield_funcs
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            if node.value.func.attr in yield_funcs:
                getattr(node.parent, node.isin).insert(node.index + 1, ast.Expr(value=ast.Yield(value=ast.Constant(value=0))))
                # We need to reindex so that further yields get the right position
                index_ast(func_ast)

    ast.fix_missing_locations(func_ast)
    # print(ast.unparse(func_ast)) # outputs the transformed code
    namespace = {}
    namespace.update(function.__globals__)
    code = compile(func_ast, "<string>", mode="exec")
    exec(code, namespace)
    return namespace[function.__name__] 

