import io
import sys


class CodeWriter(io.StringIO):
    '''
    Helper class to write code templates
    '''
    def __init__(self, opcode_module):
        super().__init__()
        self.comments = []
        self.indent_level = 0
        self.indent = 4
        self.opcode_module = opcode_module

    def ex(self, block):
        if block == None:
            # There is no next
            self.indent_level -= 1
        if not isinstance(block, dict):
            # We have a simple value
            writer.write(block)
        else:
            # We delegate to another block with an opcode
            try:
                func = getattr(self.opcode_module, block["opcode"])
                if "comments" in block:
                    self.comments.extend(block["comments"])
                func(writer)
            except:
                writer.write(f"\nNOT IMPLEMENTED: {block['opcode']}\n")
    
    def new_line(self):
        self.write("\n")
        self.write(" " * self.indent_level * self.indent)
        for c in self.comments:
            for line in c.split("\n"):
                self.write(f"# {line}")
                self.write("\n")
                self.write(" " * self.indent_level * self.indent)
        self.comments.clear()

