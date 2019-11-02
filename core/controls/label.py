from core.controls import Control


class Label(Control):
    from pygame import font
    from core.consts import Colors

    DEFAULT_FONT = font.SysFont("Calibri", 56)
    DEFAULT_COLOR = Colors.BLACK

    def __init__(self, x, y, screen, text, **props):
        super().__init__(x, y, screen)
        self.font = props.get("font", self.DEFAULT_FONT)
        self.antialias = props.get("antialias", True)
        self.color = props.get("color", self.DEFAULT_COLOR)
        self.text = text
        # TODO: Implement!
        # self.size = size

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
        self.screen.surface.blit(rendered_label, (center_x, center_y))
