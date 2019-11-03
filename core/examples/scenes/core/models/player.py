from core.examples.scenes.core.types.entities import Entity


class Player(Entity):
    def __init__(self, x, y):
        from pygame import (
            Surface,
            Color,
            Rect
        )

        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32, 32))
        self.image.fill(Color("#0000FF"))
        self.image.convert()
        self.rect = Rect(x * 32, y * 32, 32, 32)

    def update(self, up, left, right, platforms):
        if self.rect.top > 1440 or self.rect.top < 0:
            self.scene.die()
        if self.rect.left > 1408 or self.rect.right < 0:
            self.scene.die()
        if up:
            if self.onGround:
                self.yvel = 0
                self.yvel -= 10  # only jump if on the ground
        if left:
            self.xvel = -10
        if right:
            self.xvel = 10
        if not self.onGround:
            self.yvel += 0.3  # only accelerate with gravity if in the air
            if self.yvel > 80: self.yvel = 80  # max falling speed
        if not (left or right):
            self.xvel = 0

        self.rect.left += self.xvel  # increment in x direction
        if self.collide(self.xvel, 0, platforms):  # do x-axis collisions
            self.rect.top += self.yvel  # increment in y direction
            self.onGround = False;  # assuming we're in the air
            self.collide(0, self.yvel, platforms)  # do y-axis collisions

    def collide(self, xvel, yvel, platforms):
        import pygame
        from core.examples.scenes.core.models import ExitBlock

        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    self.scene.exit()
                    return False
                if xvel > 0: self.rect.right = p.rect.left
                if xvel < 0: self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        return True
