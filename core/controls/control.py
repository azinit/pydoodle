from core.types.entities import Entity
from core.types.interfaces import IHover, IColor, IClick


class Control(Entity, IHover, IColor, IClick):
    """
    Абстрактный класс для контролов
    @class Control
    @extends Entity
    """
    from core.consts import Colors

    DEFAULT_COLOR = Colors.BLACK

    def __init__(self, x, y, width, height, screen, **props):
        Entity.__init__(self, x, y, width, height, screen)
        IHover.__init__(self)
        IClick.__init__(self)
        IColor.__init__(self, props.get("color", self.DEFAULT_COLOR))

    def update(self, **props):
        import pygame
        pygame.init()
        # FIXME: Optimize?
        # mouse = props.get("mouse")

        mouse_pos = pygame.mouse.get_pos()
        left_click, _, _ = pygame.mouse.get_pressed()
        # >>> is hover?
        if self.rect.collidepoint(mouse_pos):
            self.state.on_hover = True
            if self.state.before_hover is None:
                self.state.before_hover = self.color
        else:
            if self.state.on_hover:
                self.state.on_hover = False
                self.color = self.state.before_hover

        # >>> is clicked?
        if left_click and self.rect.collidepoint(mouse_pos):
            self.state.on_click = True
            if self.state.before_click is None:
                self.state.before_click = self.color
        else:
            if self.state.on_click:
                self.state.on_click = False
                self.color = self.state.before_click

        self.activate_bindings()

    def render(self):
        raise NotImplementedError

    def on_hover(self):
        from core.consts import Colors
        if not self.state.on_click:
            self.color = Colors.lighten(self.state.before_hover, 16)

    def on_click(self):
        from core.consts import Colors
        self.color = Colors.darken(self.state.before_click, 16)
