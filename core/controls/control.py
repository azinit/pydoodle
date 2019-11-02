from core.types.entities import Entity


class Control(Entity):
    def __init__(self, x, y, screen, width=None, height=None):
        super().__init__(x, y, width, height, screen)

    def update(self, **props):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError
