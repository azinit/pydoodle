from core.controls import Control


# TODO: !!!
class Button(Control):
    DEFAULT_COLOR = Control.Colors.D_STONE
    DEFAULT_BORDER_COLOR = Control.Colors.GRAY
    DEFAULT_BORDER_WIDTH = 2
    DEFAULT_NAME = "BUTTON_{i}"
    AMOUNT = 0

    def __init__(self, x, y, width, height, screen, **props):
        super().__init__(x, y, width, height, screen, **props)
        # color = props.get("color", self.DEFAULT_COLOR)
        from core.controls import Label
        Button.AMOUNT += 1

        text = props.get("text", self.index_name)
        props.pop("text")

        self.label = Label(
            text=text,
            x=self.rect.centerx,
            y=self.rect.centery,
            screen=screen,
            **props
        )

        self.border_color = props.get("border_color", self.DEFAULT_BORDER_COLOR)
        self.border_width = props.get("border_width", self.DEFAULT_BORDER_WIDTH)

    @property
    def index_name(self):
        return self.DEFAULT_NAME.format(i=self.AMOUNT)

    def update(self, **props):
        Control.update(self)

    def render(self, outline=None):
        if outline:
            self.screen.draw.rect(self.surface, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        self.screen.draw.rect(self.surface, self.color, self.rect_tuple, 0)
        self.label.render()
