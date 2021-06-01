import inspect
import ast

class CodeBlock():
    '''
    The CodeBlock encapsulates a generator and manages its state.

    
    '''
    last_id = -1

    def add_yields(function):
        func_ast = ast.parse(inspect.getsource(function))

        for node in ast.walk(func_ast):
            if isinstance(node, ast.For):
                node.body.append(ast.Expr(value=ast.Yield(value=ast.Constant(value=1))))
        ast.fix_missing_locations(func_ast)
        namespace = {}
        code = compile(func_ast, "<string>", mode="exec")
        exec(code, namespace)
        return namespace[function.__name__] 


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
                self.generator_function = CodeBlock.add_yields(generator_function)

        # The time until the next step is executed
        self.wait_time = 0
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
            self.generator = self.generator_function(self.sprite_or_stage)
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
                self.generator_function(self.sprite_or_stage)
                print(f"CodeBlock {self.name} has finished.")
                self.running = False
                return
            else:
                try:
                    result = next(self.generator)
                    self.wait_time = 0
                    if isinstance(result, float) or isinstance(result, int):
                        self.wait_time = result
                except StopIteration:
                    print(f"CodeBlock {self.name} has finished.")
                    self.running = False

