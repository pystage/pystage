import os
from pystage.util import stderr_redirector
import sys
import io
import pygame
import pkg_resources
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

class CostumeManager():
    def __init__(self, owner):
        self.owner = owner
        self.costumes = []
        self.current_costume = -1

    def add_costume(self, name, center_x=None, center_y=None):
        if isinstance(name, str):
            costume = Costume(self, name, center_x, center_y)
            self.costumes.append(costume)
            if self.current_costume==-1:
                self.current_costume = len(self.costumes) - 1
        else:
            for n in name:
                self.add_costume(n)


    def replace_costume(self, index, name, center_x=None, center_y=None):
        costume = Costume(self, name, center_x, center_y)
        del self.costumes[index]
        self.costumes.insert(index, costume)


    def insert_costume(self, index, name, center_x=None, center_y=None):
        costume = Costume(self, name, center_x, center_y)
        self.costumes.insert(index, costume)


    def get_image(self):
        if self.current_costume == -1:
            return None
        return self.costumes[self.current_costume].image
    
    def get_center(self):
        if self.current_costume == -1:
            return None, None
        return self.costumes[self.current_costume].center_x, self.costumes[self.current_costume].center_y


class Costume():
    '''
    This class handles and manages costumes and backdrops.
    '''
    def __init__(self, sprite, name, center_x=None, center_y=None):
        self.sprite = sprite
        self.file = None
        self.name = name
        internal_folder = pkg_resources.resource_filename(__name__, "images/")
        for folder in ["", "images/", "bilder/", internal_folder]:
            for ext in ["", ".png", ".jpg", ".jpeg", ".gif", ".svg"]:
                if os.path.exists(f"{folder}{name}{ext}"):
                    self.file = f"{folder}{name}{ext}"
                    break
            if self.file is not None:
                break
        if self.file is None:
            self.file = pkg_resources.resource_filename(__name__, "images/zombie_idle.png")
        if self.file.endswith(".svg"):
            print(f"Converting SVG file: {self.file}")
            print("\nWARNING: SVG conversion is for convenience only")
            print("and might not work as expected. It is recommended")
            print("to manually convert to bitmap graphics (png or jpg).\n")
            with stderr_redirector(io.BytesIO()):
                rlg = svg2rlg(self.file)
                pil = renderPM.drawToPIL(rlg)
                self.image = pygame.image.frombuffer(pil.tobytes(), pil.size, pil.mode)
        else:
            self.image = pygame.image.load(self.file)
        self.image = self.image.subsurface(self.image.get_bounding_rect()) 
        self.center_x = self.image.get_width() / 2 if center_x is None else center_x
        self.center_y = self.image.get_height() / 2 if center_y is None else center_y


    def __str__(self):
        return f"{self.name} ({self.center_x}, {self.center_y})"
