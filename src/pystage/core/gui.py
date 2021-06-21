import pygame
import pkg_resources

pygame.init()


regular_font_14 = pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-regular.ttf"), 14)
bold_font_9 = pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-bold.ttf"), 9)
light_font_9 = pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-bold.ttf"), 9)

color1 = (87,94,117) # Text in bubbles
# Variable name bold 9
# Variable value light 9
# bubble text regular 14

class ResizableBorder():

    def __init__(self, image_file, inner_rect):
        self.image = pygame.image.load(image_file)
        self.inner_rect = inner_rect
        w = self.image.get_width()
        h = self.image.get_height()
        ix, iy, iw, ih = inner_rect
        self.ul = pygame.Surface((ix, iy), flags=pygame.SRCALPHA)
        self.top = pygame.Surface((iw, iy), flags=pygame.SRCALPHA)
        self.ur = pygame.Surface((w - (ix + iw), iy), flags=pygame.SRCALPHA)
        self.left = pygame.Surface((ix, ih), flags=pygame.SRCALPHA)
        self.center = pygame.Surface((iw, ih), flags=pygame.SRCALPHA)
        self.right = pygame.Surface((w - (ix + iw), ih), flags=pygame.SRCALPHA)
        self.bl = pygame.Surface((ix, h - (iy + ih)), flags=pygame.SRCALPHA)
        self.bottom = pygame.Surface((iw, h - (iy + ih)), flags=pygame.SRCALPHA)
        self.br = pygame.Surface((w - (ix + iw), h - (iy + ih)), flags=pygame.SRCALPHA)
        self.ul.blit(self.image, (0,0), (0, 0, self.ul.get_width(), self.ul.get_height()))
        self.top.blit(self.image, (0,0), (ix, 0, self.top.get_width(), self.top.get_height()))
        self.ur.blit(self.image, (0,0), (ix + iw, 0, self.ur.get_width(), self.ur.get_height()))
        self.left.blit(self.image, (0,0), (0, iy, self.left.get_width(), self.left.get_height()))
        self.center.blit(self.image, (0,0), (ix, iy, self.center.get_width(), self.center.get_height()))
        self.right.blit(self.image, (0,0), (ix + iw, iy, self.right.get_width(), self.right.get_height()))
        self.bl.blit(self.image, (0,0), (0, iy + ih, self.bl.get_width(), self.bl.get_height()))
        self.bottom.blit(self.image, (0,0), (ix, iy + ih, self.bottom.get_width(), self.bottom.get_height()))
        self.br.blit(self.image, (0,0), (ix + iw, iy + ih, self.br.get_width(), self.br.get_height()))
        self.min_width = self.ul.get_width() + self.ur.get_width()
        self.min_height = self.ul.get_height() + self.bl.get_height()


    def render(self, width, height):
        iw = max(width - self.min_width, 0)
        ih = max(height - self.min_height, 0)
        surface = pygame.Surface((self.min_width + iw, self.min_height + ih), flags=pygame.SRCALPHA)

        scaled_top = pygame.transform.scale(self.top, (iw, self.top.get_height()))
        surface.blit(scaled_top, (self.ul.get_width(), 0))
        scaled_bottom = pygame.transform.scale(self.bottom, (iw, self.bottom.get_height()))
        surface.blit(scaled_bottom, (self.ul.get_width(), self.ul.get_height() + ih))
        scaled_left = pygame.transform.scale(self.left, (self.left.get_width(), ih))
        surface.blit(scaled_left, (0, self.ul.get_height()))
        scaled_right = pygame.transform.scale(self.right, (self.right.get_width(), ih))
        surface.blit(scaled_right, (self.left.get_width() + iw, self.ul.get_height()))

        scaled_center = pygame.transform.scale(self.center, (iw, ih))
        surface.blit(scaled_center, (self.ul.get_width(), self.ul.get_height()))

        surface.blit(self.ul, (0, 0))
        surface.blit(self.ur, (self.ul.get_width() + iw, 0))
        surface.blit(self.bl, (0, self.ul.get_height() + ih))
        surface.blit(self.br, (self.ul.get_width() + iw, self.ul.get_height() + ih))

        return surface


def wrap_text(text, font, allowed_width):
    # See: https://stackoverflow.com/questions/49432109/how-to-wrap-text-in-pygame-using-pygame-font-font
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    max_lw = 0
    max_lh = 0
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            if len(line_words)==1:
                # Check for long words
                lw, lh = font.size(line_words[0])
                max_lh = lh
                max_lw = max(max_lw, lw)
                if lw > allowed_width:
                    max_lw = allowed_width
                    cut = []
                    while lw > allowed_width:
                        cut.append(line_words[0][-1]) 
                        line_words[0] = line_words[0][:-1]
                        lw, lh = font.size(line_words[0])
                    cut.reverse()
                    words.insert(0, "".join(cut))
                    break
            else:
                lw, lh = font.size(' '.join(line_words + words[:1]))
                if lw > allowed_width:
                    break
                max_lw = max(max_lw, lw)


        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)
        print(lines, max_lw, max_lh)
    return lines, max_lw, max_lh


def render_lines(lines, font, color, lw, lh, lh_offset):
    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    surface = pygame.Surface((lw, (lh + lh_offset) * len(lines)), flags=pygame.SRCALPHA)
    y_offset = 0
    for line in lines:
        font_surface = font.render(line, True, color)
        surface.blit(font_surface, (0, y_offset))
        y_offset += lh + lh_offset
    return surface


class BubbleManager():
    say_file = pkg_resources.resource_filename("pystage", "images/say.png")
    think_file = pkg_resources.resource_filename("pystage", "images/think.png")
    
    SAY = ResizableBorder(say_file, (18,18,154, 35))
    THINK = ResizableBorder(think_file, (18,18,154, 35))

    def __init__(self, sprite):
        self.sprite = sprite
        self.active = False
        self.text = ""
        self.border = None
        self.surface = None
        self.text_surface = None
        self.flipped = False
        self.x_offset = -0.1 # percent of sprite width based on lower right corner
        self.y_offset = -0.5 # percent of sprite height based on lower right corner

    def say(self, text: str, border=SAY):
        print(text)
        if text is None or text.strip() == "":
            self.active = False
            self.text = ""
        else:
            self.active = True
            self.text = text
            self.border = border
            lh_offset = -1
            lines, lw, lh = wrap_text(self.text[:360], regular_font_14, 170)
            self.text_surface = render_lines(lines, regular_font_14, color1, lw+10, lh, lh_offset)
            self.surface = self.border.render(self.text_surface.get_width() + 26, self.text_surface.get_height() + 40)


    def _draw(self, surface: pygame.Surface):
        if not self.active:
            return
        else:
            y = max(0, self.sprite._pg_pos()[1] - self.surface.get_height() + self.sprite.costume_manager.get_image().get_height() * self.y_offset)
            if not self.flipped:
                x = self.sprite._pg_pos()[0] - self.surface.get_width() + self.sprite.costume_manager.get_image().get_width() * self.x_offset
                if x < 0:
                    self.flipped = True
                    x = self.sprite._pg_pos()[0] - self.sprite.costume_manager.get_image().get_width() * self.x_offset
            else:
                x = self.sprite._pg_pos()[0] - self.sprite.costume_manager.get_image().get_width() * self.x_offset
                if x + self.surface.get_width() > self.sprite.stage.width:
                    self.flipped = False
                    x = self.sprite._pg_pos()[0] - self.surface.get_width() + self.sprite.costume_manager.get_image().get_width() * self.x_offset
            transformed = self.surface
            if self.flipped:
                transformed = pygame.transform.flip(self.surface, True, False)

            surface.blit(transformed, (x, y))
            surface.blit(self.text_surface, (x + 13, y + 13))

