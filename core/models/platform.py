from core.types.entities import DynamicEntity
from core.types.interfaces import IGround


# TODO: on_... interface
# TODO: implement on_floor

class Platform(DynamicEntity, IGround):
    DEFAULT_INERTIA_VAL = 4

    def __init__(self, x, y, width, height, screen, initial_state=None):
        from core.consts import Colors
        DynamicEntity.__init__(self, x, y, width, height, screen, initial_state=initial_state)
        IGround.__init__(self)

        self.elasticity = 1
        self.state.inertia_val = self.DEFAULT_INERTIA_VAL
        self.color = Colors.D_RAVEN

        self.bind("on_landed", self.on_landed)

    def update(self, **props):
        self.activate_bindings()

    def render(self):
        self.screen.draw.rect(self.surface, self.color, self.rect)

    def on_landed(self):
        # from core.consts import Colors
        # self.color = Colors.BLUE
        self.state.inertia_val -= 1
        self.rect.y += self.state.inertia_val

        if self.state.inertia_val == -self.DEFAULT_INERTIA_VAL:
            self.state.inertia_val = self.DEFAULT_INERTIA_VAL
            self.state.on_landed = False


class SuperPlatform(Platform):
    def __init__(self, x, y, width, height, screen):
        super().__init__(x, y, width, height, screen)
        from core.consts import Colors
        self.color = Colors.GRAY
        self.elasticity = 1.5


""" 
Класс платформы
@class Entity (DynamicEntity?)
"""
