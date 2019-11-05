from core.types.entities import DynamicEntity
from core.types.interfaces import IGround, ITexture


# TODO: on_... interface
# TODO: implement on_floor
class Platform(DynamicEntity, IGround, ITexture):
    DEFAULT_TEXTURE = "platform/base_diffuse.png"
    DEFAULT_SIZES = (128, 32)

    def __init__(self, x, y, width, height, screen, initial_state=None):
        from core.consts import Colors
        DynamicEntity.__init__(self, x, y, width, height, screen, initial_state=initial_state)
        IGround.__init__(self, *self.rect_tuple)
        ITexture.__init__(self, self.DEFAULT_TEXTURE, *self.rect_tuple, screen)

        self.elasticity = 1
        self.color = Colors.D_RAVEN
        self.state.visible = True

    def update(self, **props):
        scroll_up = props.get("scroll_up")
        if scroll_up:
            self.rect.move_ip(0, scroll_up)

        self.activate_bindings()

    def render(self):
        # print(self.state.visible)
        if self.state.visible:
            ITexture.render(self)
        else:
            from core.consts import Colors
            self.screen.draw.rect(self.surface, Colors.RED, self.rect_tuple)


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
