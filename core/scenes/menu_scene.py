from core.types.entities import Scene, Screen
from core.types.interfaces import ITexture


class MenuScene(Scene, ITexture):
    """
    Сцена с главным меню
    @class MenuScene
    @extends Scene
    """

    DEFAULT_BACKGROUND = "backgrounds/main_menu.jpg"

    def __init__(self, caption=None):
        Scene.__init__(self, caption=caption)
        ITexture.__init__(self, self.DEFAULT_BACKGROUND, *self.screen.rect_tuple, self.screen)
        from core.controls import Button, RecursiveBar, Label
        from core.consts import Colors

        self._controls.extend([
            Button(self.on_play, *self.screen.half_sizes, 256, 48, self.screen,
                   color=Colors.DARK, text="Play", font_size=32, font_color=Colors.WHITE),
            RecursiveBar(0, self.screen.height - 8, 16, self.screen,
                         total_value=48, current_value=0, chunks_width=128, chunks_gap=8),
            Label("Hello, ", 48, self.screen.height - 32, self.screen, color=Colors.WHITE, font_size=24),
            Label("Ilya", 96, self.screen.height - 32, self.screen, color=Colors.CYAN, font_size=24),
        ])

    """
    ..............................................................................................................
    ................................................ UPDATE ......................................................
    ..............................................................................................................
    """

    def update(self, **props):
        self._update__controls()

    def _update__controls(self):
        self._controls[1].next()
        super()._update__controls()

    """
    ..............................................................................................................
    ................................................ EVENTS ......................................................
    ..............................................................................................................
    """

    def handle_events(self, events):
        pass

    def on_play(self):
        from core.scenes import scenes
        self.screen.switch_to(scenes.game_scene)

    """
    ..............................................................................................................
    ................................................ RENDER ......................................................
    ..............................................................................................................
    """

    def render(self):
        self._render_background()
        self._render__controls()

    def _render_background(self):
        ITexture.render(self)
