from core.consts import Direction
from core.types.interfaces import IMaterial, ISpeed, IUpdate, IStateDependent


class MoveMixin(IMaterial, ISpeed, IUpdate, IStateDependent):
    """
    Миксин для возможности перемещения сущности
    @remark
    Позволяет двигать сущность с помощью метода move(*directions),
    Где в directions мы указываем направления из consts.Direction
    @example
    <pre>
        class SomeClass(MoveMixin):
            ...
        ...
        some_entity = SomeClass(...)
        ...
        # Двигаем сущность влево
        some_entity.move(Direction.LEFT)
    </pre>
    @mixin MoveMixin
    @implements IMaterial
    @todo move acceleration
    """

    DEFAULT_LIMITERS = [True, True, True, True]

    def __init__(self, x, y, width, height, dx=None, dy=None, **props):
        IMaterial.__init__(self, x, y, width, height)
        ISpeed.__init__(self, dx=dx, dy=dy)
        IStateDependent.__init__(self)
        self.ext_move = props.get("ext_move", False)
        self.move_limiters = props.get("move_limiters", self.DEFAULT_LIMITERS)
        self.state.oriented = Direction.NORMAL

    def update(self, **props):
        from pygame import (K_w, K_a, K_s, K_d)
        keys = props.get("keys")

        if keys[K_a]:
            self.move(Direction.LEFT)
            self.state.oriented = Direction.LEFT

        if keys[K_d]:
            self.move(Direction.RIGHT)
            self.state.oriented = Direction.RIGHT

        if keys[K_w] and self.ext_move:
            self.move(Direction.TOP)
            self.state.oriented = Direction.TOP

        if keys[K_s] and self.ext_move:
            self.move(Direction.BOTTOM)
            self.state.oriented = Direction.BOTTOM

    def move(self, *directions):
        for direction in directions:
            self.__move(direction)

    def __move(self, direction: Direction):
        # FIXME: Better implementation
        # FIXME: Add core/validators?
        if direction == Direction.LEFT:
            self.rect.x -= self.speed.x
        if direction == Direction.RIGHT:
            self.rect.x += self.speed.x

        if self.ext_move:
            # FIXME: was implemented as self.y -= self.speed.y
            if direction == Direction.TOP:
                self.rect.y -= self.speed.x
            if direction == Direction.BOTTOM:
                self.rect.y += self.speed.x
