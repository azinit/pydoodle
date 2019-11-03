from core.examples.scene_demo.core.types.entities import Entity


class Platform(Entity):
    def __init__(self, x, y):
        from pygame import (
            Surface,
            Rect,
        )

        Entity.__init__(self)
        # self.image = Surface([32, 32], pygame.SRCALPHA, 32) #makes blocks invisible for much better artwork
        self.image = Surface((32, 32))  # makes blocks visible for building levels
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        from pygame import (
            Surface,
            Rect,
        )

        Platform.__init__(self, x, y)
        self.image = Surface((32, 32))  # makes blocks visible for building levels
        self.image.convert()
        self.rect = Rect(x, y, 32, 32) 