from core.types.entities import Scene


class DeathScene(Scene):
    def __init__(self, caption=None, next_scene=None):
        super().__init__(caption=caption, next_scene=next_scene)
        from core.controls import Label
        from core.consts import Colors

        # from core.scenes.scenes import new_game
        # from core.scenes import GameScene
        # self.next_scene = GameScene(caption="Game | PyDoodle")
        self._controls.extend([
            Label("Try again?", *self.screen.half_sizes, screen=self.screen, color=Colors.CYAN)
        ])

    def render(self):
        self._render_background()
        self._render__controls()

    def _render_background(self):
        from core.consts import Colors
        self.surface.fill(Colors.BLACK)

    def update(self, **props):
        pass