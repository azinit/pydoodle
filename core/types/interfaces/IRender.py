class IRender:
    """
    Интерфейс "отрисовыеваемой" сущности
    @remark
    Содержит метод render()
    @interface IRender
    """
    # FIXME: Screen type
    def __init__(self, screen):
        self.screen = screen
        self.surface = screen.surface

    def render(self):
        raise NotImplementedError
