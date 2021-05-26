import io
import sys
import textwrap
import re


class CodeWriter():
    '''
    Helper class to write code templates
    '''
    def __init__(self, project, templates):
        super().__init__()
        self.project = project
        self.templates = templates

        self.comments = []
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

    def render_comments(self):
        res = ""
        for c in self.comments:
            for line in c.split("\n"):
                res += f"# {line}\n"
        self.comments.clear()
        return res

    def process(self, block):
        if not isinstance(block, dict):
            # We have a simple value
            return str(block)
        else:
            # We delegate to another block with an opcode
            res = ""
            template = ""
            if block["opcode"] in self.templates:
                if "comments" in block:
                    self.comments.extend(block["comments"])
                template = self.templates[block["opcode"]]
                res = self.render(block, template)
            else:
                res = f"\"NOT IMPLEMENTED: {block['opcode']}"
                for p in block['params']:
                    res += f" {p}"
                res += "\""
            # Continue with next block if not yet done
            if block["next"] and not "{{NEXT}}" in template:
                res += "\n"
                res += self.process(block["next"])
            return res


    def render(self, block, text):
        current_id = None
        indent_level = 0

        def reindent(text):
            nonlocal indent_level
            res = []
            for i, line in enumerate(text.split("\n")):
                if i > 0:
                    line = " " * 4 * indent_level + line
                res.append(line)
            return "\n".join(res)

        def translate(match):
            nonlocal current_id
            token = match.group(1)
            if token == "NEXT":
                return reindent(self.process(block["next"]))
            elif token =="ID":
                if not current_id:
                    current_id = self.get_id()
                return str(current_id)
            elif token == "CURRENT_SPRITE":
                return self.get_sprite_var()
            elif token in block["params"]:
                return reindent(self.process(block["params"][token]))
            else:
                raise ValueError(f"Unknown token: {token} in {text}")

        text = textwrap.dedent(text)
        lines = text.split("\n")
        res = []
        for i, line in enumerate(lines):
            indent_match = re.search(r"^[ ]*", line)
            indent_level = int(len(indent_match.group(0)) / 4)
            if i > 0 and len(lines) > 1:
                c = self.render_comments()
                if c:
                    res.append(reindent(c))
            line = re.sub(r"\{\{([^\}]+)\}\}", translate, line)
            res.append(line)

        return "\n".join(res)

