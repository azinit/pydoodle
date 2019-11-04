class ISpeed:
    DEFAULT_SPEED = 8
    DEFAULT_GRAVITY = 4
    # TODO: self.speed?

    def __init__(self, dx=None, dy=None):
        self.dx = dx or self.DEFAULT_SPEED
        self.dy = dy or self.DEFAULT_SPEED
