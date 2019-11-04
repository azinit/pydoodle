from core.types.entities import Scene


class DeathScene(Scene):
    def __init__(self, caption=None, next_scene=None):
        super().__init__(caption=caption, next_scene=next_scene)
        from core.controls import Label
        from core.consts import Colors

        self._controls.extend([
            Label(*self.screen.half_sizes(), screen=self.screen, text="You died. Try again?", color=Colors.RED)
        ])

    def render(self):
        self._render()
        self._render__controls()

    def update(self, **props):
        pass

    def _render(self):
        from core.consts import Colors
        self.surface.fill(Colors.BLACK)
