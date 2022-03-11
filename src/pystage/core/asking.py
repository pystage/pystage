import pygame
import pkg_resources

light_font_9 = pygame.font.Font(pkg_resources.resource_filename("pystage", "fonts/roboto-light.ttf"), 10)

class InputManager:

    def __init__(self, stage):
        self._queue = []
        self._answer = ""
        self._stage = stage

    @property
    def answer(self):
        return self._answer
    
    def queue(self, text, codeblock):
        question = Question(self, text, codeblock)
        self._queue.append(question)

    def is_active(self):
        return len(self._queue) > 0

    def accept_answer(self, answer):
        self._answer = answer
        del self._queue[0]
    
    def process_key(self, event):
        if self.is_active():
            self._queue[0].process_key(event)

    def update(self, dt):
        if len(self._queue) == 0:
            return
        question = self._queue[0]
        question.update(dt)


    def draw(self, surface):
        if len(self._queue) == 0:
            return
        question = self._queue[0]
        question.draw(surface)


class Question:

    OUTER_MARGIN = 5
    OUTER_HEIGHT = 55
    INNER_MARGIN = 13
    INNER_HEIGHT = 25
    GLOW = 3
    GLOW_COLOR = pygame.Color(193, 219, 255)
    ACTIVE_COLOR = pygame.Color(76, 151, 255)
    BLINK_TIME = 1

    def __init__(self, manager, text, codeblock):
        self.manager = manager
        self.text = text
        self.codeblock = codeblock
        self.answer = ""
        self.active = False
        self.stage = self.codeblock.sprite_or_stage.stage
        self.is_stage_question = self.codeblock.sprite_or_stage == self.stage
        self.blink_time = Question.BLINK_TIME
        self.cursor_visible = True
        self.rendered_answer = pygame.Surface((0,0),flags=pygame.SRCALPHA)

    def process_key(self, event):
        key = event.key
        # No CTRL stuff, leads to unknown characters
        if pygame.key.get_mods() & pygame.KMOD_CTRL:
            return
        # backspace and delete both work like backspace
        elif key == pygame.K_BACKSPACE or key == pygame.K_DELETE:
            if len(self.answer) > 0:
                self.answer = self.answer[:-1]
        # Return ends the input
        elif key == pygame.K_RETURN:
            self.manager.accept_answer(self.answer)
            self.codeblock.asking = False
            if not self.is_stage_question:
                self.codeblock.sprite_or_stage.looks_say("")
        # Add unicode representation of the pressed key to the answer
        else:
            self.answer += event.unicode
        # Update rendered text
        rendered = light_font_9.render(self.answer, True, pygame.Color(0,0,0))
        text_width = self.stage.width - 2 * Question.OUTER_MARGIN - 2 * Question.INNER_MARGIN - 36 
        cutoff = max(rendered.get_width() - text_width, 0)
        self.rendered_answer = rendered.subsurface((cutoff, 0), (min(rendered.get_width(), text_width), rendered.get_height()))

    def update(self, dt):
        if not self.active:
            self.active = True
            pygame.key.set_repeat(500, 50)
            pygame.key.start_text_input()
            if not self.is_stage_question:
                self.codeblock.sprite_or_stage.looks_say(self.text)
        self.blink_time -= dt
        if self.blink_time < 0:
            self.blink_time = Question.BLINK_TIME
            self.cursor_visible = not self.cursor_visible

    def draw(self, surface: pygame.Surface):
        area = pygame.Rect(
                Question.OUTER_MARGIN, 
                self.stage.height - Question.OUTER_HEIGHT - Question.OUTER_MARGIN, 
                self.stage.width - 2 * Question.OUTER_MARGIN, 
                Question.OUTER_HEIGHT)
        field = pygame.Rect(
                Question.OUTER_MARGIN + 2 + Question.INNER_MARGIN, 
                self.stage.height - Question.INNER_HEIGHT - Question.OUTER_MARGIN - 2 - Question.INNER_MARGIN, 
                self.stage.width - 2 * Question.OUTER_MARGIN - 2* Question.INNER_MARGIN - 4, 
                Question.INNER_HEIGHT)
        glow = pygame.Rect(field.x - Question.GLOW, field.y - Question.GLOW, field.width + 2*Question.GLOW, field.height + 2*Question.GLOW)
        pygame.draw.rect(surface, pygame.Color(200,200,200), area, 2, 5)
        pygame.draw.rect(surface, Question.GLOW_COLOR, glow, 0, 20)
        pygame.draw.rect(surface, pygame.Color(255,255,255), field, 0, 20)
        pygame.draw.rect(surface, Question.ACTIVE_COLOR, field, 1, 20)
        surface.blit(self.rendered_answer, (field.x + 15, field.y + 6))
        if self.cursor_visible:
            pygame.draw.line(surface, pygame.Color(0,0,0), (field.x + 15 + self.rendered_answer.get_width(), field.y + 8),(field.x + 15 + self.rendered_answer.get_width(), field.y + field.height - 8), 1)

