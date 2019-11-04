from core.controls import Control


class Label(Control):
    """
    Контрол Label - для отображения текста на экране
    @class Label
    @extends Control
    """

    from core.consts import Colors
    DEFAULT_COLOR = Colors.BLACK

    def __init__(self, x, y, screen, text, **props):
        super().__init__(x, y, screen, 0, 0)
        # >>> init font
        self.family = props.get("font_family", "Calibri")
        self.size = props.get("font_size", 56)
        self.bold = props.get("bold", False)
        self.italic = props.get("italic", False)
        self.font = self.generate_font(
            font_family=self.family,
            font_size=self.size,
            bold=self.bold, italic=self.italic
        )
        # >>> init other properties
        self.antialias = props.get("antialias", True)
        self.color = props.get("color", self.DEFAULT_COLOR)
        self.text = text
        # >>> re-init sizes
        self.rect.width, self.rect.height = self.sizes()

    @staticmethod
    def generate_font(font_family, font_size, **props):
        import pygame
        pygame.init()

        return pygame.font.SysFont(
            name=font_family,
            size=font_size,
            bold=props.get("bold", False),
            italic=props.get("italic", False),
        )

    def sizes(self):
        return self.font.size(self.text)

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
