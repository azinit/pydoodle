from core.types.entities import DynamicEntity, Screen
from core.mixins import (
    MoveMixin,
    GravityMixin,
    SingletonMixin,
)


# TODO: accelerate gravity
# TODO: Process state (instead of direct properties)
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
    @todo обновление/отрисовку в миксины?
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
        from core.consts import Direction
        self.state.oriented = Direction.NORMAL

    def update(self, **props):
        from pygame import (K_w, K_a, K_s, K_d)
        keys = props.get("keys")
        platforms = props.get("platforms", [])
        GravityMixin.update(self, keys=keys, grounds=platforms)

        # TODO: implement to MoveMixin
        from core.consts import Direction

        # FIXME: Optimize?
        # >>> LEFT
        # if keys[pygame.K_a] and not self.left_border_passed:
        if keys[K_a]:
            if self.left_border_passed:
                self.drop_right()
            self.move(Direction.LEFT)
            self.state.oriented = Direction.LEFT
        # >>> RIGHT
        # if keys[pygame.K_d] and not self.right_border_passed:
        if keys[K_d]:
            if self.right_border_passed:
                self.drop_left()
            self.move(Direction.RIGHT)
            self.state.oriented = Direction.RIGHT
        # else:
        #     self.state.oriented = Direction.NORMAL

        if self.ext_move:
            # >>> UP
            if keys[K_w] and not self.top_border_passed:
                self.move(Direction.TOP)
                self.state.oriented = Direction.TOP
            # >>> DOWN
            if keys[K_s] and not self.bottom_border_passed:
                self.move(Direction.BOTTOM)
                self.state.oriented = Direction.BOTTOM

        # FIXME: Optimize?
        if self.state.is_jumping:
            self.state.oriented = Direction.TOP
        if self.state.is_falling:
            self.state.oriented = Direction.BOTTOM

    def render(self):
        import pygame

        from core.consts import Colors, Direction

        # FIXME: Temporary!
        color = Colors.D_STONE
        # if self.state.oriented == Direction.LEFT:
        #     color = Colors.darken(color, 16)
        # if self.state.oriented == Direction.RIGHT:
        #     color = Colors.lighten(color, 16)
        # if self.state.oriented == Direction.UP:
        #     color = Colors.lighten(color, 32)
        # if self.state.oriented == Direction.DOWN:
        #     color = Colors.darken(color, 32)

        pygame.draw.rect(self.surface, color, self.rect)
        # print(type(Colors.CYAN))
