from core.types.entities import Entity


class Control(Entity):
    """
    Абстрактный класс для контролов
    @class Control
    @extends Entity
    """

    def __init__(self, x, y, screen, width, height):
        super().__init__(x, y, width, height, screen)

    def update(self, **props):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError
