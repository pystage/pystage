import math
import os
import random
# from pystage.util import stderr_redirector
import sys
import io
import pygame
import pkg_resources
import pystage
from pystage.core.values import is_number, to_number

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
        # The rendered image is only updated when something changed.
        self._cache_key = None
        self._cached_center = pygame.Vector2(0, 0)
        self._cached_backdrop = None


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

    def previous_costume(self):
        if self.current_costume == -1:
            return
        self.current_costume -= 1
        if self.current_costume == -1:
            self.current_costume = len(self.costumes) - 1
        self.update_sprite_image()

    def random_costume(self):
        if self.current_costume == -1:
            return
        self.current_costume = random.randint(0, len(self.costumes)-1)
        self.update_sprite_image()

    def has_costume(self, name):
        return any(costume.name.lower().strip() == str(name).lower().strip() for costume in self.costumes)

    def switch_costume(self, name):
        if not self.costumes:
            return
        # A name always wins, even if it looks like a number.
        if not isinstance(name, (int, float)) or isinstance(name, bool):
            for i, costume in enumerate(self.costumes):
                if costume.name.lower().strip() == str(name).lower().strip():
                    self.current_costume = i
                    self.update_sprite_image()
                    return
            if not is_number(name):
                return
        # Scratch also supports numbers here, starting with 1.
        self.current_costume = (int(round(to_number(name))) - 1) % len(self.costumes)
        self.update_sprite_image()

    def _effects(self):
        o = self.owner
        return (o.color, o.fisheye, o.whirl, o.pixelate, o.mosaic, o.brightness, o.ghost)

    def update_sprite_image(self):
        if isinstance(self.owner, pystage.core.CoreStage):
            return
        if self.current_costume == -1:
            return
        owner = self.owner
        direction = owner._direction % 360
        if self.rotation_style == CostumeManager.NO_ROTATION:
            direction = 0
        elif self.rotation_style == CostumeManager.LEFT_RIGHT:
            direction = 180 if 90 < direction < 270 else 0
        key = (id(self.costumes[self.current_costume]), direction, owner.size, self._effects())
        if key != self._cache_key:
            image, new_center = self.process_image()
            self._cache_key = key
            self._cached_center = _round(new_center)
            owner.image = image
            owner.mask = pygame.mask.from_surface(image)
            if owner.stage.show_sprite_boundaries:
                c = self._cached_center
                image.blit(owner.mask.to_surface(), (0,0))
                pygame.draw.rect(image, "red", image.get_rect(), 1)
                pygame.draw.line(image, "red", c - (10, 0), c + (10, 0), 1)
                pygame.draw.line(image, "red", c - (0, 10), c + (0, 10), 1)
        owner.rect = owner.image.get_rect()
        owner.rect.topleft = _round(owner._pos) - self._cached_center

    def get_backdrop(self):
        """The rendered backdrop and its position on the stage."""
        costume = self.get_costume()
        if costume is None:
            return None, (0, 0)
        key = (id(costume), self._effects())
        if key != self._cache_key:
            self._cache_key = key
            self._cached_backdrop = self.run_processors(costume.image.copy())
        stage = self.owner
        return self._cached_backdrop, (round(stage.center_x - costume.center_x), round(stage.center_y - costume.center_y))

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


    def process_image(self):
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

        # Very small or negative sizes are not possible
        scale = max(self.owner.size, 1) / 100


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


        rendered_image = self.run_processors(rotozoom_image)
        return rendered_image, new_center
    
    def run_processors(self, image: pygame.Surface):
        rendered_image = self.color_processor(image)
        rendered_image = self.fisheye_processor(rendered_image)
        rendered_image = self.whirl_processor(rendered_image)
        rendered_image = self.pixelate_processor(rendered_image)
        rendered_image = self.mosaic_processor(rendered_image)
        rendered_image = self.brightness_processor(rendered_image)
        rendered_image = self.ghost_processor(rendered_image)
        return rendered_image

    def color_processor(self, image: pygame.Surface):
        value = self.owner.color
        if value == 0:
            return image
        bg_img = pygame.Surface(image.get_size(), flags=pygame.SRCALPHA)
        bg_img.fill(self.gen_color(self.owner.color % 200))
        bg_img.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return bg_img

    def fisheye_processor(self, image: pygame.Surface):
        value = self.owner.fisheye
        if value == 0:
            return image
        value = max(0, 1 + value / 100)
        width, height = image.get_size()
        center_x = width // 2
        center_y = height // 2

        distorted_image = pygame.Surface((width, height), pygame.SRCALPHA)

        for x in range(width):
            dx = x - center_x
            dx2 = dx ** 2
            for y in range(height):
                dy = y - center_y
                distance = math.sqrt(dx2 + dy**2)
                if distance < center_x:
                    r = distance / center_x
                    theta = math.atan2(dy, dx)
                    distortion_radius = r ** value * center_x
                    distorted_x = int(
                        center_x + distortion_radius * math.cos(theta)
                    )
                    distorted_y = int(
                        center_y + distortion_radius * math.sin(theta)
                    )
                    if 0 <= distorted_x < width and 0 <= distorted_y < height:
                        pixel_color = image.get_at((distorted_x, distorted_y))
                        distorted_image.set_at((x, y), pixel_color)
                else:
                    pixel_color = image.get_at((x, y))
                    distorted_image.set_at((x, y), pixel_color)
        return distorted_image

    def whirl_processor(self, image: pygame.Surface):
        value = self.owner.whirl
        if value == 0:
            return image

        w, h = image.get_size()
        cx, cy = w // 2, h // 2

        distorted_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)

        for x in range(w):
            dx = x - cx
            dx2 = dx ** 2
            for y in range(h):
                dy = y - cy
                distance = math.sqrt(dx2 + dy ** 2)

                if distance < cx:
                    angle = value * 0.1 * (cx - distance) / cx
                    new_x = int(cx + math.cos(angle)
                                * dx - math.sin(angle) * dy)
                    new_y = int(cy + math.sin(angle)
                                * dx + math.cos(angle) * dy)
                    if 0 <= new_x < image.get_width() and 0 <= new_y < image.get_height():
                        distorted_image.set_at(
                            (x, y), image.get_at((new_x, new_y)))

                else:
                    distorted_image.set_at((x, y), image.get_at((x, y)))
        return distorted_image

    def pixelate_processor(self, image: pygame.Surface):
        value = abs(self.owner.pixelate) // 12
        if value == 0:
            return image
        w, h = image.get_size()
        image = pygame.transform.scale(image, (max(1, w // value), max(1, h // value)))
        image = pygame.transform.scale(image, (w, h))
        return image

    def mosaic_processor(self, image: pygame.Surface):
        value = abs(self.owner.mosaic)
        if value == 0:
            return image
        # algorithm of tiles in scratch
        # https://scratch.mit.edu/discuss/topic/112886/?page=1#post-992766
        tiles = max(1, int((value + 15) // 10))
        if tiles == 1:
            return image
        w, h = image.get_size()
        new_image = pygame.Surface((w, h), pygame.SRCALPHA)
        new_size = pygame.Vector2(int(image.get_width() / tiles), int(image.get_height() / tiles))
        image = pygame.transform.scale(image, new_size)
        copies = []
        for _ in range(tiles**2-1):
            copies.append(image.copy())

        copies.append(image)

        x, y = 0, 0
        row = tiles
        cur_row = 1
        cur_col = 1
        for image in copies:
            new_image.blit(image, (x, y))
            cur_row += 1
            x += w/tiles
            if cur_row > row:
                cur_row = 1
                cur_col += 1
                x = 0
                y += h/tiles
        return new_image

    def brightness_processor(self, image: pygame.Surface):
        value = max(-100, min(self.owner.brightness, 100))
        if value == 0:
            return image
        amount = int(abs(value) * 255 / 100)
        result = image.copy()
        flag = pygame.BLEND_RGB_ADD if value > 0 else pygame.BLEND_RGB_SUB
        result.fill((amount, amount, amount), special_flags=flag)
        return result

    def ghost_processor(self, image: pygame.Surface):
        ghost = max(0, min(self.owner.ghost, 100))
        if ghost == 0:
            return image
        result = image.copy()
        alpha = int((100 - ghost) / 100 * 255)
        result.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MULT)
        return result

    def gen_color(self, value):
        if value >= 0 and value <= 50:
            green = int((value / 50) * 255)
            return 155, green, 60
        elif value >= 51 and value <= 100:
            blue = int(((value - 50) / 50) * 255)
            return 60, 155, blue
        elif value >= 101 and value <= 150:
            red = int(((value - 100) / 50) * 255)
            return red, 50, 200
        elif value >= 151 and value <= 200:
            blue = int(((value - 150) / 50) * 255)
            return 200, 50, blue
        else:
            raise ValueError("Invalid value. Must be between 0 and 200.")


class Costume():
    '''
    This class handles and manages costumes and backdrops.
    '''
    def __init__(self, sprite, name, center_x=None, center_y=None, factor=1):
        self.sprite = sprite
        self.file = None
        self.name = name
        internal_folder = pkg_resources.resource_filename("pystage", "images/")
        # Add further folders for translations here
        named_folders = ["", "images/", "bilder/"]
        # Folders relative to CWD
        search_folders = named_folders.copy()
        # Folders relative to python script
        for folder in named_folders:
            search_folders.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), folder))
        # Internal default sprites
        search_folders.append(internal_folder)

        for folder in search_folders:
            for ext in ["", ".bmp", ".png", ".jpg", ".jpeg", ".gif", ".svg"]:
                if os.path.exists(f"{folder}{name}{ext}"):
                    # Check if the file can actually be loaded
                    # It could e.g. be a directory with the same name as we allow no ending
                    try:
                        filename = f"{folder}{name}{ext}"
                        self.image = pygame.image.load(filename)
                        self.file = filename
                        break
                    except Exception:
                        pass
            if self.file is not None:
                break
        if self.file is None:
            self.file = pkg_resources.resource_filename("pystage", "images/zombie_idle.png")
            self.image = pygame.image.load(self.file)
        if self.file.endswith(".svg"):
            print("\nWARNING: SVG conversion is for convenience only")
            print("and might not work as expected. It is recommended")
            print("to manually convert to bitmap graphics (png or jpg).\n")
        if pygame.display.get_surface() is not None:
            self.image = self.image.convert_alpha()
        if factor!=1:
            self.image = pygame.transform.rotozoom(self.image, 0, 1.0/factor)
        bounding_rect = self.image.get_bounding_rect()
        if bounding_rect.width == 0 or bounding_rect.height == 0:
            # Completely transparent image
            bounding_rect = pygame.Rect(0, 0, 1, 1)
        self.image = self.image.subsurface(bounding_rect)
        # The offset resulting from the image crop
        offset = pygame.Vector2(self.image.get_offset())
        self.center_x = (float(self.image.get_parent().get_width()) / 2) - offset.x if center_x is None else (float(center_x) / factor) - offset.x 
        self.center_y = (float(self.image.get_parent().get_height()) / 2) - offset.y if center_y is None else (float(center_y) / factor) - offset.y


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

    def get_sound(self, name, pitch=0):
        """Get the pygame sound, None if it does not exist or can't be played."""
        if name not in self.sounds:
            if isinstance(name, (int, float)) and self.sounds:
                # Scratch also supports numbers here, starting with 1.
                name = list(self.sounds)[(int(round(name)) - 1) % len(self.sounds)]
            else:
                # Sounds can be used without adding them explicitly
                name = str(name)
                self.add_sound(name)
        return self.sounds[name].get(pitch)


class Sound():
    '''
    This class handles and manages sounds.
    '''
    def __init__(self, sprite, name):
        self.name = name
        self.sprite = sprite
        self.file = None
        self.sound = None
        # pitch: sound
        self._pitched = {}
        internal_folder = pkg_resources.resource_filename("pystage", "sounds/")
        # Add further folders for translations here
        named_folders = ["", "sounds/", "klaenge/"]
        # Folders relative to CWD
        search_folders = named_folders.copy()
        # Folders relative to python script
        for folder in named_folders:
            search_folders.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), folder))
        # Internal default sprites
        search_folders.append(internal_folder)

        for folder in search_folders:
            for ext in ["", ".wav", ".ogg", ".mp3"]:
                if os.path.isfile(f"{folder}{name}{ext}"):
                    self.file = f"{folder}{name}{ext}"
                    break
            if self.file is not None:
                break
        if self.file is None:
            print(f"WARNING: Sound '{name}' not found.")
        elif pygame.mixer.get_init():
            try:
                self.sound = pygame.mixer.Sound(self.file)
            except pygame.error as e:
                print(f"WARNING: Sound '{name}' can't be loaded, try to convert it to wav or ogg format. ({e})")


    def get(self, pitch=0):
        """The sound with the pitch effect of Scratch applied.

        A pitch of 10 is a half-step, 120 an octave. Like in Scratch, this
        also changes the speed of the sound. Needs numpy.
        """
        if self.sound is None or pitch == 0:
            return self.sound
        pitch = max(-360, min(360, round(pitch)))
        if pitch not in self._pitched:
            try:
                import numpy
                samples = pygame.sndarray.array(self.sound)
                ratio = 2 ** (pitch / 120)
                positions = numpy.arange(0, len(samples), ratio)
                indices = numpy.minimum(positions.astype(int), len(samples) - 1)
                self._pitched[pitch] = pygame.sndarray.make_sound(numpy.ascontiguousarray(samples[indices]))
            except Exception:
                # numpy is optional
                self._pitched[pitch] = self.sound
        return self._pitched[pitch]


    def __str__(self):
        return f"{self.name}"
