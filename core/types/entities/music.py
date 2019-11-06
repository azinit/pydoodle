from core.types.interfaces import IPlay, IPause, IStop


# FIXME: Tone Fix for music!!

class Music(IPlay, IPause, IStop):
    PATH_TO_MUSIC = "resources/music"

    def __init__(self, source):
        IPlay.__init__(self)
        IPause.__init__(self)
        IStop.__init__(self)

        import pygame
        pygame.init()

        self.src = source
        self.__mixer = pygame.mixer
        self.__music = pygame.mixer.music.load(self.path)
        self.is_playing = False

    def play(self, **props):
        self.is_playing = True
        self.__mixer.music.play(-1)

    def set_volume(self, value: float):
        self.__mixer.music.set_volume(value)

    def pause(self):
        self.is_playing = False
        pass

    def stop(self):
        self.is_playing = False
        pass

    @property
    def path(self):
        return "{root}/{src}".format(
            root=self.PATH_TO_MUSIC,
            src=self.src,
        )
