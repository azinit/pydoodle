import abc

from core.consts import Direction

_DEFAULT_SPEED = 4

# TODO: ReImplement! (more Abstract)


class Movable(abc.ABC):
    def __init__(self, x, y, dx=None, dy=None):
        self.x = x
        self.y = y
        self.dx = dx or _DEFAULT_SPEED
        self.dy = dy or _DEFAULT_SPEED

    @property
    def pos(self):
        return tuple((self.x, self.y))

    def move(self, *directions):
        for direction in directions:
            self.__move(direction)

    def __move(self, direction: Direction):
        # TODO: Better implementation
        # TODO: Add core/validators?
        if direction == Direction.LEFT:
            self.x -= self.dx
        if direction == Direction.RIGHT:
            self.x += self.dx
        if direction == Direction.UP:
            self.y -= self.dy
        if direction == Direction.DOWN:
            self.y += self.dy
