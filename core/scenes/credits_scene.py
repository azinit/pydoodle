from core.types.entities import Scene


class CreditsScene(Scene):
    THREAD = "CREDITS_SCENE"

    def __init__(self, label_text, caption=None, next_scene=None):
        super().__init__(caption=caption, next_scene=next_scene)

        from core.controls import Label
        from core.consts import Colors
        print("Press Space to go next")

        hz = self.screen.half_sizes()

        # >>> Init Controls
        self._credit = Label(*hz, self.screen, label_text, color=Colors.WHITE)
        self._controls.extend([
            self._credit
        ])

    def render(self):
        self._render()
        self._render__controls()

    def update(self, **props):
        # super().update(**props)
        from core.modules import console
        import pygame
        keys = props.get("keys")
        # if keys[pygame.K_SPACE]:
        #     console.log("TO GAME >>>", thread=self.THREAD)
        #     from core.scenes import GameScene
        #     self.screen.switch_to()

        # if keys[pygame.K_RIGHT]:
        #     print("R")
        #     self._credit.update(text=self._credit.text + ".")
        # if keys[pygame.K_LEFT]:
        #     print("L")
        #     self._credit.update(text=self._credit.text[:-1])

    def handle_events(self, events):
        super().handle_events(events)

    def _render(self):
        from core.consts import Colors
        self.screen.surface.fill(Colors.BLACK)
