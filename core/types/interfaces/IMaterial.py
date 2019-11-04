# FIXME: -> AbstractClass?
# FIXME: Collide implement through velocity


class IMaterial:
    """
    Интерфейс "материальной" сущности
    @remark
    Содержит базовые свойства осязаемой сущности (x, y, width, height)
    Дает доступ
    @interface IMaterial
    """

    def __init__(self, x, y, width, height):
        import pygame
        self.rect = pygame.Rect((x, y, width, height))

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    @property
    def rect_tuple(self):
        return tuple((
            self.x,
            self.y,
            self.width,
            self.height
        ))

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

    # def collide(self, another):
    #     if self.is_collide_with(another):
    #         by_top = self.is_collide_by_top(another)
    #         by_bottom = self.is_collide_by_bottom(another)
    #         by_left = self.is_collide_by_left(another)
    #         by_right = self.is_collide_by_right(another)
    #         inside = self.is_inside_of(another)
    #
    #         print("T: {T} | B: {B} | L: {L} | R: {R} | I: {I}".format(
    #             T=int(by_top),
    #             B=int(by_bottom),
    #             L=int(by_left),
    #             R=int(by_right),
    #             I=int(inside),
    #         ))
    #
    #     return None

    def collide(self, another):
        """
        Сначала - проверяем коллизию снизу (для блокировки)
        Затем, по бокам (для столкновения)
        А в конце уже - коллизию сверху (для отскока)
        :param another:
        :return:
        """
        from core.consts import Direction
        # FIXME: Implement better? (SIDE-BOTTOM case)

        # dirs = [
        #     int(self.is_collide_by_right(another)),
        #     int(self.is_collide_by_top(another)),
        #     int(self.is_collide_by_left(another)),
        #     int(self.is_collide_by_bottom(another)),
        # ]
        #
        # if sum(dirs) != 1:
        #     print("DOUBLE!")
        #     return None
        if not self.is_collide_with(another):
            return None

        if self.is_collide_by_bottom(another):
            self.rect.top = another.rect.bottom
            return Direction.BOTTOM

        if self.is_collide_by_left(another):
            self.rect.right = another.rect.left
            return Direction.LEFT
        if self.is_collide_by_right(another):
            self.rect.left = another.rect.right
            return Direction.RIGHT

        if self.is_collide_by_top(another):
            self.rect.bottom = another.rect.top
            return Direction.TOP

        return None

    def is_collide_with(self, another):
        "https://github.com/search?q=pygame.Rect.colliderect&type=Code&l=Python"
        "https://kite.com/python/docs/pygame.Rect"
        return self.rect.colliderect(another.rect)

    def is_collide_by_top(self, another):
        by_top = (self.rect.bottom >= another.rect.top) and (self.rect.top <= another.rect.top)
        return self.is_collide_with(another) and by_top

    def is_collide_by_bottom(self, another):
        by_bottom = (self.rect.top <= another.rect.bottom) and (self.rect.bottom >= another.rect.bottom)
        return self.is_collide_with(another) and by_bottom

    def is_collide_by_left(self, another):
        by_left = (self.rect.right >= another.rect.left) and (self.rect.left <= another.rect.left)
        return self.is_collide_with(another) and by_left

    def is_collide_by_right(self, another):
        by_right = (self.rect.left <= another.rect.right) and (self.rect.right >= another.rect.right)
        return self.is_collide_with(another) and by_right

    def is_inside_of(self, another):
        return another.rect.contains(self.rect)
