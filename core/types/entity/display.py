# TODO: Singletone
from core.types.entity.scene import Scene


class Display(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        import pygame
        self.window = pygame.display.set_mode(self.sizes)

    @property
    def sizes(self):
        return tuple((self.width, self.height))

    def render(self):
        from core.consts import Colors
        self.window.fill(Colors.DARK)

    def set_scene(self, scene: Scene):
        pass

    # TODO: scenes integration
    # TODO: Is object on stage (not out of border)