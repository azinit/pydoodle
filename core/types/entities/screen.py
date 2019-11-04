from core.mixins import SingletonMixin


# TODO: Is object on stage (not out of border)
# FIXME: class Screen(Surface):
# FIXME: Fade In/Out:
#  https://stackoverflow.com/questions/52856030/how-to-fade-in-and-out-a-text-in-pygame

class Screen(SingletonMixin):
    """
    Экран/Дисплей игры
    @remark
    1. Доступ к основному экрану получается через Screen#get_global
    2. Позволяет обращаться к текущей сцене через SCREEN.scene.<your_method>
    3. Служит в роли SceneManager
    @class
    @remark
    @implements ISceneManager (реализую позже сам интерфейс)
    @mixin SingletonMixin
    @see SingletonMixin
    """
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
        """ Задать заголовок окну """
        import pygame
        pygame.display.set_caption(caption)

    @property
    def rect(self):
        """ Обратиться к Screen как к pygame.Rect """
        from pygame import Rect
        return Rect(*self.rect_tuple)

    @property
    def rect_tuple(self):
        return tuple((
            0,
            0,
            self.width,
            self.height
        ))

    @property
    def sizes(self):
        """ Получить размеры Screen """
        return tuple((self.width, self.height))

    def switch_to(self, scene):
        """ Переключиться на сцену (scene) """
        self.scene = scene

    def half_sizes(self):
        """ Получить половинные размеры """
        return tuple((self.width // 2, self.height // 2))

    @property
    def draw(self):
        import pygame
        return pygame.draw

    @property
    def blit(self):
        # TODO: Implement
        raise NotImplementedError
    # Deprecated! Will be removed soon!
    # def render(self):
    #     self.scene.render()
    #
    # def update(self, **props):
    #     self.scene.update(**props)
    #
    # def handle_events(self, events):
    #     self.scene.handle_events(events)
