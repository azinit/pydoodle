from core.consts import Direction
from core.types.interfaces import IMaterial


class MoveMixin(IMaterial):
    DEFAULT_SPEED = 8

    def __init__(self, x, y, width, height, dx=None, dy=None, **props):
        super().__init__(x, y, width, height)
        self.dx = dx or self.DEFAULT_SPEED
        self.dy = dy or self.DEFAULT_SPEED
        self.ext_move = props.get("ext_move", False)

    def move(self, *directions):
        for direction in directions:
            self.__move(direction)

    def __move(self, direction: Direction):
        # FIXME: Better implementation
        # FIXME: Add core/validators?
        if direction == Direction.LEFT:
            self.x -= self.dx
        if direction == Direction.RIGHT:
            self.x += self.dx

        if self.ext_move:
            if direction == Direction.UP:
                self.y -= self.dy
            if direction == Direction.DOWN:
                self.y += self.dy