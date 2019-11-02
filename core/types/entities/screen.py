# TODO: Singletone


# TODO: Is object on stage (not out of border)
# FIXME: class Screen(Surface):

class Screen(object):
    DEFAULT_CAPTION = "[dev] PyDoodle"
    __GLOBAL_INSTANCE = None

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

    @staticmethod
    def get_global():
        if Screen.__GLOBAL_INSTANCE is None:
            from core.consts import ScreenSize
            Screen.__GLOBAL_INSTANCE = Screen(*ScreenSize.WXGA)

        return Screen.__GLOBAL_INSTANCE

    # def render(self):
    #     self.scene.render()
    #
    # def update(self, **props):
    #     self.scene.update(**props)
    #
    # def handle_events(self, events):
    #     self.scene.handle_events(events)
