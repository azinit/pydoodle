import abc


class IMaterial(abc.ABC):
    def __init__(self, x, y, width, height, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface

    @property
    def rect_tuple(self):
        return tuple((
            self.x,
            self.y,
            self.width,
            self.height
        ))

    @property
    def rect(self):
        from pygame.rect import Rect
        return Rect(self.rect_tuple)

    @property
    def pos(self):
        return tuple((
            self.x,
            self.y
        ))

    def is_collide_with(self, another):
        "https://github.com/search?q=pygame.Rect.colliderect&type=Code&l=Python"
        "https://kite.com/python/docs/pygame.Rect"
        return self.rect.colliderect(another.rect)

    # @classmethod
    # def are_collide(one, another):
    #     return one.is_collide_with(another)
