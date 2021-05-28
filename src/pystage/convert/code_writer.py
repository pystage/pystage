import io
import sys
import textwrap
import re
import logging
from jinja2 import Template, Environment
logger = logging.getLogger(__name__)


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
        self.jinja_environment = Environment(trim_blocks=True, lstrip_blocks=True)
        self.jinja_environment.filters["global_sound"] = lambda name: self.global_sound(name)
        self.jinja_environment.filters["global_costume"] = lambda name: self.global_costume(name)
        self.jinja_environment.filters["global_backdrop"] = lambda name: self.global_backdrop(name)
        
        logger.debug("CodeWriter created.")


    def set_sprite(self, name):
        self.current_sprite = name


    def get_sprite_var(self, name=None):
        def to_python(name: str):
            return name.lower().replace(" ", "_"). replace("-", "_")
        if name is None:
            return to_python(self.current_sprite)
        else:
            return to_python(name)

    def get_sprite_or_stage(self, name=None):
        if not name:
            name = self.current_sprite
        if self.project["stage"]["name"] == name:
            return self.project["stage"]
        for sprite in self.project["sprites"]:
            if sprite["name"]==name:
                return sprite
        raise ValueError(f"No stage or sprite found with name '{name}'.")

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

    def global_sound(self, name):
        name = name.replace('"', '')
        sprite = self.get_sprite_or_stage()
        for sound in sprite["sounds"]:
            if sound["local_name"] == name:
                return f'"{self.project["sounds"][sound["md5"]]["global_name"]}"'
        raise ValueError(f"No sound with name '{name}' found for sprite '{sprite['name']}'")
        

    def global_costume(self, name):
        name = name.replace('"', '')
        sprite = self.get_sprite_or_stage()
        for costume in sprite["costumes"]:
            if costume["local_name"] == name:
                return f'"{self.project["costumes"][costume["md5"]]["global_name"]}"'
        raise ValueError(f"No costume with name '{name}' found for sprite '{sprite['name']}'")

    def global_backdrop(self, name):
        name = name.replace('"', '')
        sprite = self.project["stage"]
        for costume in sprite["costumes"]:
            if costume["local_name"] == name:
                return f'"{self.project["costumes"][costume["md5"]]["global_name"]}"'
        raise ValueError(f"No backdrop with name '{name}' found for stage.")


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
            return res


    def render(self, block, text):
        text = textwrap.dedent(text)
        context = {}
        if block["next"]:
            context["NEXT"] = self.process(block["next"])
            if not "NEXT" in text:
                text += "\n{{NEXT}}"
        for param in block["params"]:
            context[param] = self.process(block["params"][param])
        context["CURRENT_SPRITE"] = self.get_sprite_var()
        if "{{ID}}" in text:
            context["ID"] = self.get_id()
        template = self.jinja_environment.from_string(text)
        text = template.render(context)
        return text

