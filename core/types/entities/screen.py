from core.mixins import SingletonMixin


#

# TODO: Is object on stage (not out of border)
# FIXME: class Screen(Surface):

class Screen(SingletonMixin):
    from core.consts import ScreenSize

    DEFAULT_CAPTION = "[dev] PyDoodle"

    DEFAULT_SIZES = ScreenSize.WXGA
    DEFAULT_PROPS = {
        "width": DEFAULT_SIZES[0],
        "height": DEFAULT_SIZES[1],
    }

    def __init__(self, width, height):
        import pygame

        self.width = width
        self.height = height
        self.caption = self.DEFAULT_CAPTION
        self.surface = pygame.display.set_mode(self.sizes)
        self.set_caption(self.caption)
        self.scene = None

    @staticmethod
    def set_caption(caption):
        import pygame
        pygame.display.set_caption(caption)

    @property
    def rect(self):
        from pygame import Rect
        return Rect((
            0,
            0,
            self.width,
            self.height
        ))

    @property
    def sizes(self):
        return tuple((self.width, self.height))

    def switch_to(self, scene):
        self.scene = scene

    def half_sizes(self):
        return tuple((self.width // 2, self.height // 2))
    # def render(self):
    #     self.scene.render()
    #
    # def update(self, **props):
    #     self.scene.update(**props)
    #
    # def handle_events(self, events):
    #     self.scene.handle_events(events)
