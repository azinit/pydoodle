from core.types.entities import DynamicEntity, Screen
from core.mixins import (
    MoveMixin,
    JumpMixin,
    SingletonMixin,
)


# MAX_JUMP_COUNT = 10
# TODO: Process state (instead of direct properties)
class Player(DynamicEntity, MoveMixin, JumpMixin, SingletonMixin):
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
        "y": 425,
        "width": 60,
        "height": 71,
        "screen": Screen.get_global()
    }

    def __init__(self, x, y, width, height, screen, dx=None, dy=None):
        DynamicEntity.__init__(self, x, y, width, height, screen, initial_state=self.DEFAULT_STATE)
        MoveMixin.__init__(self, x, y, width, height, dx, dy, ext_move=True)

    def update(self, **props):
        import pygame

        keys = props.get("keys")
        # >>> handle keys

        if keys[pygame.K_SPACE]:
            self.is_jump = True

        # TODO: Switch!
        # TODO: to Mixins?
        # >>> Left
        from core.consts import Direction
        if keys[pygame.K_a] and not self.left_border_passed:
            self.move(Direction.LEFT)
        if keys[pygame.K_d] and not self.right_border_passed:
            self.move(Direction.RIGHT)
        if keys[pygame.K_w] and not self.top_border_passed:
            self.move(Direction.UP)
        if keys[pygame.K_s] and not self.bottom_border_passed:
            self.move(Direction.DOWN)

        # >>> update
        if self.is_jump:
            self.jump()

    def render(self):
        import pygame

        from core.consts import Colors
        pygame.draw.rect(self.screen.surface, Colors.WHITE, self.rect)
        # print(type(Colors.CYAN))
