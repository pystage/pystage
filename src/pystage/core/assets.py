import math
import os
import random
import subprocess
# from pystage.util import stderr_redirector
import sys
import io
import pygame
import pkg_resources
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import pystage
import soundfile

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

    def switch_costume(self, name):
        if name == "next backdrop":
            self.next_costume()
            return
        if name == "previous backdrop":
            self.previous_costume()
            return
        if name == "random backdrop":
            self.random_costume()
            return
        for i, costume in enumerate(self.costumes):
            if costume.name.lower().strip() == name.lower().strip():
                self.current_costume = i
                self.update_sprite_image()
                return

    def update_sprite_image(self):
        if isinstance(self.owner, pystage.core.CoreStage):
            return
        image, new_center = self.process_image()
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

    def get_costume_name(self):
        if self.current_costume == -1:
            return None
        return self.costumes[self.current_costume].name

    
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
        bg_img = pygame.Surface(image.get_size()).convert_alpha()
        bg_img.fill(self.gen_color(self.owner.color))
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
        image = pygame.transform.scale(image, (w / value, h / value))
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

        image = pygame.transform.scale_by(image, 1/tiles)
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
        value = self.owner.brightness
        if value == 0:
            return image
        brightened_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        brightened_image.blit(image, (0, 0))
        for x in range(brightened_image.get_width()):
            for y in range(brightened_image.get_height()):
                pixel = brightened_image.get_at((x, y))
                r, g, b, a = pixel

                if value > 0:
                    r += (255 - r) * value // 100
                    g += (255 - g) * value // 100
                    b += (255 - b) * value // 100
                elif value < 0:
                    r -= r * abs(value) // 100
                    g -= g * abs(value) // 100
                    b -= b * abs(value) // 100

                r = max(0, min(r, 255))
                g = max(0, min(g, 255))
                b = max(0, min(b, 255))

                brightened_image.set_at((x, y), (r, g, b, a))

        return brightened_image
    
    def ghost_processor(self, image: pygame.Surface):
        image.set_alpha((100-self.owner.ghost)/100*255)
        return image
    
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
        for folder in ["", "images/", "bilder/", internal_folder]:
            for ext in ["", ".bmp", ".png", ".jpg", ".jpeg", ".gif", ".svg"]:
                if os.path.exists(f"{folder}{name}{ext}"):
                    self.file = f"{folder}{name}{ext}"
                    break
            if self.file is not None:
                break
        if self.file is None:
            self.file = pkg_resources.resource_filename("pystage", "images/zombie_idle.png")
        # if self.file.endswith(".svg"):
        #     print(f"Converting SVG file: {self.file}")
        #     print("\nWARNING: SVG conversion is for convenience only")
        #     print("and might not work as expected. It is recommended")
        #     print("to manually convert to bitmap graphics (png or jpg).\n")
        #     # Deactivated for now because of Windows problems. See issue #10
        #     # with stderr_redirector(io.BytesIO()):
        #     rlg = svg2rlg(self.file)
        #     pil = renderPM.drawToPIL(rlg)
        #     self.image = pygame.image.frombuffer(pil.tobytes(), pil.size, pil.mode)
        # else:
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
        self.sounds: dict[str, Sound] = {}

    def add_sound(self, name):
        if isinstance(name, str):
            sound = Sound(self, name)
            self.sounds[name]=sound
        else:
            for n in name:
                self.add_sound(n)

    def get_sound(self, name, pitch):
        if pitch == 0:
            return self.sounds[name].sound
        sound = self.sounds[name].get_sound_with_pitch(pitch)
        if sound:
            os.unlink(self.sounds[name].pitched_file)
        return sound


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

            path, suf = self.file.rsplit(".", 1)
            self.pitched_file = f"{path}_pitched.{suf}"


    def get_sound_with_pitch(self, pitch, keep_length=False):
        """
        Pitch from -360 to 360
        10 is a half-step
        120 is an octave

        From: https://en.scratch-wiki.info/wiki/Sound_Effect
            Right now the pitch effect works by changing the speed of the sound, although in the future the Scratch Team may change it back to only affecting a sound's pitch.
        
        So I leave a parameter for keeping the length of the audio.
        """
        if not self.sound:
            return None
        
        pitch = max(-360, min(360, pitch))
        half_steps = pitch / 10
        rate_factor = 2.0 ** (half_steps / 12.0)
        original_rate = self.get_framerate()
        new_rate = round(original_rate * rate_factor, 5)
        tempo = max(0.5, min(100, round(1.0 / rate_factor, 5)))
        if keep_length:
            parameters = "asetrate={},atempo={}".format(new_rate, tempo)
        else:
            parameters = "asetrate={}".format(new_rate)
        conversion_command = ["ffmpeg", "-i", self.file, "-af", parameters, self.pitched_file, "-y"]

        with open(os.devnull, 'rb') as devnull:
            p = subprocess.Popen(conversion_command, stdin=devnull, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p_out, p_err = p.communicate()
        if p.returncode != 0:
            print(f"Can't change pitch of sound file: {self.file}")
            return self.sound
        
        return pygame.mixer.Sound(self.pitched_file)
    
    def get_framerate(self):
        with soundfile.SoundFile(self.file) as f:
            framerate = f.samplerate
        return framerate


    def __str__(self):
        return f"{self.name}"
