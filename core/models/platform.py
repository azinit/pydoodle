from core.types.entities import DynamicEntity
from core.types.interfaces import IGround, ITexture


# TODO: on_... interface
# TODO: implement on_floor
class Platform(DynamicEntity, IGround, ITexture):
    DEFAULT_TEXTURE = "platform/base_diffuse.png"

    def __init__(self, x, y, width, height, screen, initial_state=None):
        from core.consts import Colors
        DynamicEntity.__init__(self, x, y, width, height, screen, initial_state=initial_state)
        IGround.__init__(self, *self.rect_tuple)
        ITexture.__init__(self, self.DEFAULT_TEXTURE, *self.rect_tuple, screen)

        self.elasticity = 1
        self.color = Colors.D_RAVEN

    def update(self, **props):
        self.activate_bindings()

    def render(self):
        ITexture.render(self)


class SuperPlatform(Platform):
    DEFAULT_TEXTURE = "platform/super_diffuse.png"

    def __init__(self, x, y, width, height, screen):
        super().__init__(x, y, width, height, screen)
        from core.consts import Colors
        self.color = Colors.GRAY
        self.elasticity = 1.5


""" 
Класс платформы
@class Entity (DynamicEntity?)
"""
