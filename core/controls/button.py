from core.controls import Control


class Button(Control):
    from core.consts import Colors
    DEFAULT_COLOR = Colors.D_STONE
    DEFAULT_BORDER_COLOR = Colors.GRAY
    DEFAULT_BORDER_WIDTH = 2
    DEFAULT_NAME = "BUTTON_{i}"
    AMOUNT = 0

    def __init__(self, handler, x, y, width, height, screen, **props):
        super().__init__(x, y, width, height, screen,
                         color=props.get("color", self.DEFAULT_COLOR))
        from core.controls import Label
        Button.AMOUNT += 1

        if props.get("auto_center", True):
            self.rect.x -= self.width // 2
            self.rect.y -= self.height // 2

        text = props.get("text", self.index_name)

        # FIXME:
        props.pop("text")
        if "color" in props.keys():
            props.pop("color")

        # >>> init btn_label
        self.label = Label(
            text=text,
            x=self.rect.centerx,
            y=self.rect.centery,
            screen=screen,
            color=props.get("font_color", Label.DEFAULT_COLOR),
            **props
        )

        self.border_color = props.get("border_color", self.DEFAULT_BORDER_COLOR)
        self.border_width = props.get("border_width", self.DEFAULT_BORDER_WIDTH)
        self.bind("on_click", handler)

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
