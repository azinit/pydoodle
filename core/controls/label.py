from core.controls import Control


class Label(Control):
    """
    Контрол Label - для отображения текста на экране
    @class Label
    @extends Control
    @todo Label#font() - метод для генерации стиля
    @todo Label(size=...) - поле в конструкторе для указания размера текста
    """
    import pygame
    pygame.init()

    from core.consts import Colors

    DEFAULT_FONT = pygame.font.SysFont("Calibri", 56)
    DEFAULT_COLOR = Colors.BLACK

    def __init__(self, x, y, screen, text, **props):
        self.font = props.get("font", self.DEFAULT_FONT)
        self.antialias = props.get("antialias", True)
        self.color = props.get("color", self.DEFAULT_COLOR)
        self.text = text

        # FIXME:
        super().__init__(x, y, screen, *self.sizes)
        # TODO: Implement!
        # self.size = size

    @property
    def sizes(self):
        return self.font.render(self.text, self.antialias, self.color).get_size()

    def update(self, **props):
        new_text = props.get("text")

        if new_text:
            self.text = new_text

    def render(self):
        rendered_label = self.font.render(self.text, self.antialias, self.color)
        # >>> centering label
        actual_sizes = rendered_label.get_size()
        center_x = self.x - actual_sizes[0] // 2
        center_y = self.y - actual_sizes[1] // 2
        # >>> snap to surface
        self.surface.blit(rendered_label, (center_x, center_y))
