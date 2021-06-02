import os
import pygame
import pkg_resources


class Costume():
    '''
    This class handles and manages costumes and backdrops.
    '''
    def __init__(self, sprite, name, center_x=None, center_y=None):
        self.sprite = sprite
        self.file = None
        self.name = name
        for folder in [".", "./images", "./bilder"]:
            for ext in ["", ".png", ".jpg", ".jpeg", ".gif"]:
                if os.path.exists(f"{name}{ext}"):
                    self.file = f"{name}{ext}"
                    break
            if self.file is not None:
                break
        if self.file is None:
            self.file = pkg_resources.resource_filename(__name__, "images/zombie_idle.png")
        self.image = pygame.image.load(self.file)
        self.center_x = self.image.get_width() / 2 if center_x is None else center_x
        self.center_y = self.image.get_height() / 2 if center_y is None else center_y


    def __str__(self):
        return f"{self.name} ({self.center_x}, {self.center_y})"


    def _draw(self):
        sprite = self.sprite
        stage = self.sprite.stage
        # Rotation
        # Scratch is clockwise with 0 upwards
        # pyGame is counterclockwise with 0 to the right
        transformed = pygame.transform.rotate(self.image, 90-sprite.direction)
        # keep the center stable when the image size changes
        # TODO: this is only correct when the rotation center is at the center
        # This is currently always the case with Scratch
        # Otherwise, it gets more complicated, the goal would be that the center point
        # remains stable within the image, i.e. if we have it for instance on an eye,
        # it remains on the eye during all transformations.
        offset_x = (self.image.get_width() - transformed.get_width()) / 2
        offset_y = (self.image.get_height() - transformed.get_height()) / 2
        stage.screen.blit(transformed, (sprite.x + stage.center_x - self.center_x + offset_x, sprite.y + stage.center_y - self.center_y + offset_y))


