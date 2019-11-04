from core.consts import Direction
from core.types.interfaces import IMaterial, ISpeed, IUpdate


class MoveMixin(IMaterial, ISpeed, IUpdate):
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

    def __init__(self, x, y, width, height, dx=None, dy=None, **props):
        IMaterial.__init__(self, x, y, width, height)
        ISpeed.__init__(self, dx=dx, dy=dy)
        self.ext_move = props.get("ext_move", False)

    # TODO: Implement!
    # def update(self, **props):
    #     from pygame import (
    #         K_a,
    #         K_d,
    #         K_w,
    #         K_s
    #     )
    #
    #     keys = props.get("keys")
    #     from core.consts import Direction
    #     if keys[K_a] and not self.left_border_passed:
    #         self.move(Direction.LEFT)
    #     if keys[K_d] and not self.right_border_passed:
    #         self.move(Direction.RIGHT)
    #     if keys[K_w] and not self.top_border_passed:
    #         self.move(Direction.UP)
    #     if keys[K_s] and not self.bottom_border_passed:
    #         self.move(Direction.DOWN)

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
            # was implementad as self.y -= self.speed.y
            # FIXME: !!!

            if direction == Direction.TOP:
                self.rect.y -= self.speed.x
            if direction == Direction.BOTTOM:
                self.rect.y += self.speed.x
