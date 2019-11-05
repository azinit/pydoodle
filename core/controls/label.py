from core.controls import Control


class Label(Control):
    """
    Контрол Label - для отображения текста на экране
    @class Label
    @extends Control
    """

    def __init__(self, text, x, y, screen, **props):
        super().__init__(x, y, 0, 0, screen, **props)
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

    # FIXME:
    # @property
    # def image(self):
    #     return self.rendered_label

    def sizes(self):
        return self.font.size(self.text)

    def update(self, **props):
        new_text = props.get("text")

        if new_text:
            self.text = new_text

    @property
    def rendered_label(self):
        return self.font.render(self.text, self.antialias, self.color)

    @property
    def center(self):
        actual_sizes = self.rendered_label.get_size()
        center_x = self.x - actual_sizes[0] // 2
        center_y = self.y - actual_sizes[1] // 2
        return tuple((center_x, center_y))

    def render(self):
        self.surface.blit(self.rendered_label, self.center)
