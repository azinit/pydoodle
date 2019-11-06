from core.types.entities import Scene
from core.types.interfaces import ITexture


class CreditsScene(Scene, ITexture):
    """
    Сцена с титрами
    @class CreditsScene
    @extends Scene
    """

    THREAD = "CREDITS_SCENE"

    def __init__(self, label_text, texture, caption=None, next_scene=None):
        Scene.__init__(self, caption=caption, next_scene=next_scene)
        ITexture.__init__(self, texture, *self.screen.half_sizes, self.screen.width, self.screen.height,
                          self.screen, auto_scale=False)

        img_x, img_y = self.image.get_size()
        self.rect.move_ip(- img_x // 2, - img_y // 2)
        from core.controls import Label
        from core.consts import Colors
        from core.modules import console
        console.log("Press Space to go next", thread=self.THREAD)

        hz = self.screen.half_sizes

        # >>> Init Controls
        # self._credit = Label(label_text, *hz, self.screen, color=Colors.WHITE, font_size=50)
        self._controls.extend([
            # self._credit
        ])

    def render(self):
        self._render_background()
        self._render__controls()

    def _render_background(self):
        """ Отрисовка бэкграунда """
        from core.consts import Colors
        self.screen.surface.fill(Colors.BLACK)
        ITexture.render(self)

    def update(self, **props):
        # TOIMPLEMENT
        # super().update(**props)
        from core.modules import console
        import pygame

        # props = {
        #     "keys": [...],
        #     "events": []
        # }
        # keys = props.get("keys")
        # if keys[pygame.K_SPACE]:
        #     console.log("TO GAME >>>", thread=self.THREAD)
        #     from core.scene_demo import GameScene
        #     self.screen.switch_to()

        # if keys[pygame.K_RIGHT]:
        #     print("R")
        #     self._credit.update(text=self._credit.text + ".")
        # if keys[pygame.K_LEFT]:
        #     print("L")
        #     self._credit.update(text=self._credit.text[:-1])

    def handle_events(self, events):
        super().handle_events(events)


