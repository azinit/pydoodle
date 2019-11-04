from core.types.entities import DynamicEntity, Screen
from core.mixins import (
    MoveMixin,
    GravityMixin,
    SingletonMixin,
)


class Player(DynamicEntity, MoveMixin, GravityMixin, SingletonMixin):
    """
    Класс - игрок
    Базовый класс для управления игроком(дудлом) в игре и главном меню
    @class Player
    @extends DynamicEntity
    @mixin MoveMixin
    @mixin JumpMixin
    @mixin SingletonMixin
    @todo Один игрок для меню и игры?
    """

    DEFAULT_PROPS = {
        "x": 50,
        "y": 100,
        "width": 32,
        "height": 32,
        "screen": Screen.get_global()
    }

    def __init__(self, x, y, width, height, screen, dx=None, dy=None):
        DynamicEntity.__init__(self, x, y, width, height, screen, initial_state=self.DEFAULT_STATE)
        MoveMixin.__init__(self, x, y, width, height, dx, dy, ext_move=False)
        GravityMixin.__init__(self, x, y, width, height, is_bouncing=True)

    def update(self, **props):
        from pygame import (K_a, K_d)
        keys = props.get("keys")

        GravityMixin.update(self, **props)
        MoveMixin.update(self, **props)
        if keys[K_a] and self.left_border_passed:
            self.drop_right()
        if keys[K_d] and self.right_border_passed:
            self.drop_left()

        # Not need?
        # if self.state.is_jumping:
        #     self.state.oriented = Direction.TOP
        # if self.state.is_falling:
        #     self.state.oriented = Direction.BOTTOM

    def render(self):
        from core.consts import Colors
        color = Colors.D_STONE

        # Not need?
        # if self.state.oriented == Direction.LEFT:
        #     color = Colors.darken(color, 16)
        # if self.state.oriented == Direction.RIGHT:
        #     color = Colors.lighten(color, 16)
        # if self.state.oriented == Direction.UP:
        #     color = Colors.lighten(color, 32)
        # if self.state.oriented == Direction.DOWN:
        #     color = Colors.darken(color, 32)

        self.screen.draw.rect(self.surface, color, self.rect)
