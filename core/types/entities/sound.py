from core.types.interfaces import IPlay


# TODO: enums/sounds

class Sound(IPlay):
    PATH_TO_SOUNDS = "resources/sounds"

    def __init__(self, source):
        import pygame
        pygame.init()

        self.src = source
        self.__mixer = pygame.mixer
        self.__sound = pygame.mixer.Sound(self.path)

    def play(self, **props):
        self.__sound.play()

    @property
    def path(self):
        return "{root}/{src}".format(
            root=self.PATH_TO_SOUNDS,
            src=self.src,
        )


"""
resources/sounds/kick.mp3
resources/sounds/kick.mp3
"""
