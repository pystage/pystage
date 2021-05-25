import io
import sys


class CodeWriter(io.StringIO):
    '''
    Helper class to write code templates
    '''
    def __init__(self, project, opcode_module):
        super().__init__()
        self.comments = []
        self.indent_level = 0
        self.indent = 4
        self.opcode_module = opcode_module
        self.last_id = 0
        self.current_sprite = ""


    def set_sprite(self, name):
        self.current_sprite = name


    def get_sprite_var(self, name=None):
        def to_python(name: str):
            return name.lower().replace(" ", "_"). replace("-", "_")
        if name is None:
            return to_python(self.current_sprite)
        else:
            return to_python(name)


    def get_id(self):
        '''
        Helper to create unique names
        '''
        self.last_id += 1
        return self.last_id

    def next_or_pass(self, block):
        if block["next"]:
            self.ex(block["next"])
        else:
            self.write("pass")
            self.newline()

    def ex(self, block):
        if not isinstance(block, dict):
            # We have a simple value
            self.write(block)
        else:
            # We delegate to another block with an opcode
            if hasattr(self.opcode_module, block["opcode"]):
                func = getattr(self.opcode_module, block["opcode"])
                if "comments" in block:
                    self.comments.extend(block["comments"])
                func(self, block)
            else:
                self.write(f"\nNOT IMPLEMENTED: {block['opcode']}\n")
    
    def newline(self, num=1):
        for i in range(num):
            self.write("\n")
            self.write(" " * self.indent_level * self.indent)
        for c in self.comments:
            for line in c.split("\n"):
                self.write(f"# {line}")
                self.write("\n")
                self.write(" " * self.indent_level * self.indent)
        self.comments.clear()

