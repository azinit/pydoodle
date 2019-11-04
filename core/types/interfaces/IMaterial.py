# FIXME: -> AbstractClass?


class IMaterial:
    """
    Интерфейс "материальной" сущности
    @remark
    Содержит базовые свойства осязаемой сущности (x, y, width, height)
    Дает доступ
    @interface IMaterial
    """

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

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

    @property
    def pos_int(self):
        return tuple((
            int(self.x),
            int(self.y),
        ))

    def is_collide_with(self, another):
        "https://github.com/search?q=pygame.Rect.colliderect&type=Code&l=Python"
        "https://kite.com/python/docs/pygame.Rect"
        return self.rect.colliderect(another.rect)

    def is_landed_on(self, potential_ground):
        are_collide_as_ground = self.rect.bottom >= potential_ground.rect.top
        # FIXME: !!!
        not_collide_as_jumped = self.rect.top <= potential_ground.rect.bottom
        # print(self.rect.bottom, potential_ground.rect.top)
        return self.is_collide_with(potential_ground) and are_collide_as_ground and not_collide_as_jumped

    # @classmethod
    # def are_collide(one, another):
    #     return one.is_collide_with(another)
