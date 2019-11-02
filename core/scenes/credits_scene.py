from core.types.entities import Scene


class CreditsScene(Scene):
    THREAD = "CREDITS_SCENE"

    def __init__(self, caption=None):
        super().__init__(caption=caption)
        from core.modules import console
        print("Press Space to start game")

    def render(self):
        self.__render()

    def update(self, **props):
        from core.modules import console
        import pygame
        keys = props.get("keys")
        if keys[pygame.K_SPACE]:
            console.log("TO GAME >>>", thread=self.THREAD)
            from core.scenes import GameScene
            self.screen.switch_to(GameScene(
                caption="Game | PyDoodle"
            ))

    def handle_events(self, events):
        # for e in events:
        #     if e.type ==
        pass

    def __render(self):
        from core.consts import Colors
        self.screen.surface.fill(Colors.CYAN)
