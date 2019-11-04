from core.types.entities import DynamicEntity, Screen
from core.mixins import (
    MoveMixin,
    GravityMixin,
    SingletonMixin,
)


# TODO: accelerate gravity
# MAX_JUMP_COUNT = 10
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
    DEFAULT_STATE = {
        "is_jump": False,
        "is_move": False,
        "oriented_left": False,
        "oriented_right": False,
    }

    DEFAULT_PROPS = {
        "x": 50,
        "y": 100,
        "width": 32,
        "height": 32,
        "screen": Screen.get_global()
    }

    def __init__(self, x, y, width, height, screen, dx=None, dy=None):
        DynamicEntity.__init__(self, x, y, width, height, screen, initial_state=self.DEFAULT_STATE)
        MoveMixin.__init__(self, x, y, width, height, dx, dy, ext_move=True)
        GravityMixin.__init__(self, x, y, width, height)

    def update(self, **props):
        import pygame

        keys = props.get("keys")
        platforms = props.get("platforms", [])
        GravityMixin.update(self, keys=keys, grounds=platforms)

        # TODO: implement to MoveMixin
        from core.consts import Direction
        if keys[pygame.K_a] and not self.left_border_passed:
            self.move(Direction.LEFT)
        if keys[pygame.K_d] and not self.right_border_passed:
            self.move(Direction.RIGHT)
        if keys[pygame.K_w] and not self.top_border_passed:
            self.move(Direction.UP)
        if keys[pygame.K_s] and not self.bottom_border_passed:
            self.move(Direction.DOWN)

    def render(self):
        import pygame

        from core.consts import Colors
        pygame.draw.rect(self.surface, Colors.CYAN, self.rect)
        # print(type(Colors.CYAN))
