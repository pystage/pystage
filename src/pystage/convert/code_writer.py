import io
import sys
import textwrap


class CodeWriter(io.StringIO):
    '''
    Helper class to write code templates
    '''
    def __init__(self, project, opcode_module):
        super().__init__()
        self.project = project
        self.opcode_module = opcode_module

        self.comments = []
        self.indent_level = 0
        self.indent = 4
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

    def write_next_or_pass(self, block):
        if block["next"]:
            self.ex(block["next"])
        else:
            self.write("pass")
            self.newline()

    def get_next_or_pass(self, block, indent=0):
        inner = CodeWriter(self.project, self.opcode_module)
        inner.indent_level = indent
        inner.write_next_or_pass(block)
        return inner.getvalue()

    def ex(self, block):
        if not isinstance(block, dict):
            # We have a simple value
            self.write(str(block))
        else:
            # Flag the block so that it does not get written twice
            if "done" in block and block["done"]:
                return
            block["done"] = True

            # We delegate to another block with an opcode
            if hasattr(self.opcode_module, block["opcode"]):
                func = getattr(self.opcode_module, block["opcode"])
                if "comments" in block:
                    self.comments.extend(block["comments"])
                func(self, block)
            else:
                self.newline()
                self.write(f"NOT IMPLEMENTED: {block['opcode']}")
                for p in block['params']:
                    self.write(f" {p}")
                self.newline()
            if block["next"]:
                self.ex(block["next"])

    def get_ex(self, block, indent=0):
        inner = CodeWriter(self.project, self.opcode_module)
        inner.indent_level = indent
        inner.ex(block)
        return inner.getvalue()

    def write_block(self, text:str, before=0, after=0):
        for i in range(before):
            self.newline()
        redent = textwrap.indent(textwrap.dedent(text), " " * self.indent_level * self.indent)
        self.write(redent)
        if text.endswith("\n"):
            self.write_indent()
            self.write_comments()
        for i in range(after):
            self.newline()

    def write_line(self, text:str, before=0, after=0):
        for i in range(before):
            self.newline()
        self.write(text)
        for i in range(after+1):
            self.newline()

    def write_comments(self):
        for c in self.comments:
            for line in c.split("\n"):
                self.write(f"# {line}")
                self.write("\n")
                self.write_indent()
        self.comments.clear()

    def write_indent(self):
        self.write(" " * self.indent_level * self.indent)
    
    def newline(self, after=0):
        for i in range(after+1):
            self.write("\n")
            self.write_indent()
        self.write_comments()

