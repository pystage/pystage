import os
# from pystage.util import stderr_redirector
import sys
import io
import pygame
import pkg_resources
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import pystage

_round = lambda v: pygame.Vector2(round(v.x), round(v.y))

class CostumeManager():

    ALL_AROUND = 1
    LEFT_RIGHT = 2
    NO_ROTATION = 3

    def __init__(self, owner):
        self.owner = owner
        self.costumes = []
        self.current_costume = -1
        self.rotation_style = CostumeManager.ALL_AROUND

    def add_costume(self, name, center_x=None, center_y=None, factor=1):
        if isinstance(name, str):
            costume = Costume(self, name, center_x, center_y, factor)
            self.costumes.append(costume)
            if self.current_costume==-1:
                self.current_costume = len(self.costumes) - 1
                self.update_sprite_image()
        else:
            for n in name:
                self.add_costume(n)


    def replace_costume(self, index, name, center_x=None, center_y=None, factor=1):
        costume = Costume(self, name, center_x, center_y, factor)
        del self.costumes[index]
        self.costumes.insert(index, costume)
        self.update_sprite_image()


    def insert_costume(self, index, name, center_x=None, center_y=None, factor=1):
        costume = Costume(self, name, center_x, center_y, factor)
        self.costumes.insert(index, costume)
        self.update_sprite_image()

    def next_costume(self):
        if self.current_costume == -1:
            return
        self.current_costume += 1
        if self.current_costume == len(self.costumes):
            self.current_costume = 0
        self.update_sprite_image()

    def switch_costume(self, name):
        for i, costume in enumerate(self.costumes):
            if costume.name.lower().strip() == name.lower().strip():
                self.current_costume = i
                self.update_sprite_image()
                return

    def update_sprite_image(self):
        if isinstance(self.owner, pystage.core.CoreStage):
            return
        image, new_center = self.rotate_and_scale()
        self.owner.image = image
        self.owner.mask = pygame.mask.from_surface(image)
        self.owner.rect = image.get_rect()
        self.owner.rect.topleft = _round(self.owner._pos) - new_center
        new_center = _round(new_center)
        if self.owner.stage.show_sprite_boundaries:
            image.blit(self.owner.mask.to_surface(), (0,0))
            pygame.draw.rect(image, "red", image.get_rect(), 1)
            pygame.draw.line(image, "red", new_center - (10, 0), new_center + (10, 0), 1)
            pygame.draw.line(image, "red", new_center - (0, 10), new_center + (0, 10), 1)


    def get_image(self):
        if self.current_costume == -1:
            return None
        return self.costumes[self.current_costume].image


    def get_costume(self):
        if self.current_costume == -1:
            return None
        return self.costumes[self.current_costume]

    
    def get_center(self):
        if self.current_costume == -1:
            return 0, 0
        return pygame.Vector2(self.costumes[self.current_costume].center_x, self.costumes[self.current_costume].center_y)


    def rotate_and_scale(self):
        # Based on:
        # https://stackoverflow.com/questions/54462645/how-to-rotate-an-image-around-its-center-while-its-scale-is-getting-largerin-py
        # Rotation settings
        flipped = False
        if self.rotation_style == CostumeManager.ALL_AROUND:
            angle = self.owner._direction
        elif self.rotation_style == CostumeManager.NO_ROTATION:
            angle = 0
        else: # LEFT_RIGHT
            angle = 0
            flipped = True if 90 < self.owner._direction % 360 < 270 else False 

        # Zoom settings
        scale = self.owner.size / 100

        old_center = self.get_center()
        old_center.y *= -1
        center_rotated = old_center.rotate(angle)

        # Corner points of the current rect
        w, h = self.get_image().get_size()
        box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        
        # Axis aligned bounding box
        minx = min(box_rotate, key=lambda p: p[0])[0]
        maxx = max(box_rotate, key=lambda p: p[0])[0]
        miny = min(box_rotate, key=lambda p: p[1])[1]
        maxy = max(box_rotate, key=lambda p: p[1])[1]
        topleft = pygame.Vector2(minx, maxy)

        # new center
        new_center = center_rotated - topleft
        new_center.y *= -1
        new_center *= scale

        # get a rotated image
        rotozoom_image = pygame.transform.rotozoom(self.get_image(), angle, scale)
        if flipped:
            rotozoom_image = pygame.transform.flip(rotozoom_image, True, False)


        return rotozoom_image, new_center


class Costume():
    '''
    This class handles and manages costumes and backdrops.
    '''
    def __init__(self, sprite, name, center_x=None, center_y=None, factor=1):
        self.sprite = sprite
        self.file = None
        self.name = name
        internal_folder = pkg_resources.resource_filename("pystage", "images/")
        for folder in ["", "images/", "bilder/", internal_folder]:
            for ext in ["", ".bmp", ".png", ".jpg", ".jpeg", ".gif", ".svg"]:
                if os.path.exists(f"{folder}{name}{ext}"):
                    self.file = f"{folder}{name}{ext}"
                    break
            if self.file is not None:
                break
        if self.file is None:
            self.file = pkg_resources.resource_filename("pystage", "images/zombie_idle.png")
        if self.file.endswith(".svg"):
            print(f"Converting SVG file: {self.file}")
            print("\nWARNING: SVG conversion is for convenience only")
            print("and might not work as expected. It is recommended")
            print("to manually convert to bitmap graphics (png or jpg).\n")
            # Deactivated for now because of Windows problems. See issue #10
            # with stderr_redirector(io.BytesIO()):
            rlg = svg2rlg(self.file)
            pil = renderPM.drawToPIL(rlg)
            self.image = pygame.image.frombuffer(pil.tobytes(), pil.size, pil.mode)
        else:
            self.image = pygame.image.load(self.file)
        if factor!=1:
            self.image = pygame.transform.rotozoom(self.image, 0, 1.0/factor)
        self.image = self.image.subsurface(self.image.get_bounding_rect()) 
        # The offset resulting from the image crop
        offset = pygame.Vector2(self.image.get_offset())
        self.center_x = (float(self.image.get_parent().get_width()) / 2) - offset.x if center_x is None else (float(center_x) / factor) - offset.x 
        self.center_y = (float(self.image.get_parent().get_height()) / 2) - offset.y if center_y is None else (float(center_y) / factor) - offset.y
        print(f"New costume: {name} -> {self.file}")


    def __str__(self):
        return f"{self.name} ({self.center_x}, {self.center_y})"


class SoundManager():
    def __init__(self, owner):
        self.owner = owner
        self.sounds = {}

    def add_sound(self, name):
        if isinstance(name, str):
            sound = Sound(self, name)
            self.sounds[name]=sound
        else:
            for n in name:
                self.add_sound(n)

    def get_sound(self, name):
        return self.sounds[name].sound


class Sound():
    '''
    This class handles and manages sounds.
    '''
    def __init__(self, sprite, name):
        self.name = name
        self.sprite = sprite
        self.file = None
        self.sound = None
        internal_folder = pkg_resources.resource_filename("pystage", "sounds/")
        for folder in ["", "sounds/", "klaenge/", internal_folder]:
            for ext in ["", ".wav", ".ogg", ".mp3"]:
                if os.path.exists(f"{folder}{name}{ext}"):
                    self.file = f"{folder}{name}{ext}"
                    break
            if self.file is not None:
                break
        if self.file.endswith(".mp3"):
            print("WARNING: MP3 is not supported in pyStage. Use wav or ogg format.")
        elif self.file is not None:
            self.sound = pygame.mixer.Sound(self.file)


    def __str__(self):
        return f"{self.name}"
