from core.types.interfaces import (
    IRender,
    IUpdate,
    IHandleEvents,
)


# FIXME: Caption "captin | PyDoodl "

class Scene(IRender, IUpdate, IHandleEvents):
    """
    Класс - Сцена
    Реализует базовое поведение и свойства сцены игры
    @class Scene
    @implements IRender
    @implements IUpdate
    @implements IHandleEvents
    @see Screen
    """
    THREAD = "SCENE"

    def __init__(self, caption=None, next_scene=None):
        from core.types.entities import Screen
        IRender.__init__(self, Screen.get_global())
        self.caption = caption or self.screen.caption
        self.screen.set_caption(self.caption)
        self.next_scene = next_scene
        self._controls = []

    def render(self):
        raise NotImplementedError

    def update(self, **props):
        # import pygame
        # keys = props.get("keys")
        #
        # if keys[pygame.K_SPACE]:
        #     if self.next_scene:
        #         self.screen.switch_to(self.next_scene)
        raise NotImplementedError

    def handle_events(self, events):
        import pygame
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                if self.next_scene:
                    self.screen.switch_to(self.next_scene)

    def _render_background(self):
        """ Как правило, служит для пре-отрисовки перед отрисовкой контролов и моделей """
        raise NotImplementedError

    def _render__controls(self):
        """ Отображение всех контролов на сцене """
        for _control in self._controls:
            _control.render()

    def _update__controls(self):
        for _control in self._controls:
            _control.update()
