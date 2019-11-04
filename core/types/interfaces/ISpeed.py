class ISpeed:
    DEFAULT_SPEED = 8
    DEFAULT_GRAVITY = 4

    def __init__(self, **speed):
        from types import SimpleNamespace
        self.speed = SimpleNamespace()
        self.speed.x = speed.get("dx") or self.DEFAULT_SPEED
        self.speed.y = speed.get("dy") or 0
