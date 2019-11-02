from core.types.entities import Scene, Screen


class MenuScene(Scene):
    def __init__(self, screen: Screen):
        super().__init__(screen)

    def render(self):
        pass

    def update(self, **props):
        pass

    def handle_events(self, events):
        pass
