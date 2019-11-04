from core.types.entities import DynamicEntity, Screen
from core.mixins import (
    MoveMixin,
    GravityMixin,
    SingletonMixin,
)
from core.types.interfaces import ISequenceSprite


class Player(DynamicEntity, MoveMixin, GravityMixin, SingletonMixin, ISequenceSprite):
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
        "width": 64,
        "height": 64,
        "screen": Screen.get_global()
    }

    DEFAULT_TEXTURE = "doodle/base_diffuse.png"
    DEFAULT_SPRITE = "doodle/seq-sprite_{i}.png"

    def __init__(self, x, y, width, height, screen, dx=None, dy=None):
        DynamicEntity.__init__(self, x, y, width, height, screen)
        MoveMixin.__init__(self, *self.rect_tuple, dx, dy, ext_move=False)
        GravityMixin.__init__(self, *self.rect_tuple, is_bouncing=True)

        animation_data = ISequenceSprite.animation_data(4, self.DEFAULT_SPRITE)
        ISequenceSprite.__init__(self, self.DEFAULT_SPRITE, animation_data, *self.rect_tuple, screen,
                                 fr_amount=2, fr_iter=8)

    def update(self, **props):
        from pygame import (K_a, K_d)
        keys = props.get("keys")

        ISequenceSprite.update(self, **props)
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

        # self.screen.draw.rect(self.surface, color, self.rect)
        ISequenceSprite.render(self)


# TODO StateSequenceSprite

data = [
    # if in <state> => load sprites_pack
    {
        "property": "oriented",
        "value": "Direction.LEFT",
        "frame": {
            "amount": 4,
            "pattern": "doodle/test-sprite_left_{i}.png"
        }
    },
    {
        "property": "oriented",
        "value": "Direction.RIGHT",
        "frame": {
            "amount": 4,
            "pattern": "doodle/test-sprite_right_{i}.png"
        }
    },
    {
        "property": "oriented",
        "value": "Direction.NORMAL",
        "frame": {
            "amount": 2,
            "pattern": "doodle/test-sprite_normal_{i}.png"
        }
    },
    {
        "property": "is_fly",
        "value": True,
        "frame": {
            "amount": 2,
            "pattern": "doodle/test-sprite_fly_{i}.png"
        }
    }
]
