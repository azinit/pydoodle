class IRender:
    # FIXME: Screen type
    def __init__(self, screen):
        self.screen = screen

    def render(self):
        raise NotImplementedError
