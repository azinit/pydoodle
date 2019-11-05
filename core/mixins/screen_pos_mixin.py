from core.types.interfaces import IMaterial


class ScreenPosMixin(IMaterial):
    """
    Миксин для получения информации об материальном объекте относительно экрана
    @example
    <pre>
        class SomeClass(ScreenPosMixin):
            ...

        # получение информации об объекте
        some_entity = SomeClass(...)
        ...
        # Перемещаем сущность налево, если она еще не доходила до левой границы
        if key[K_LEFT} and not some_entity.left_border_passed:
            move(Direction.LEFT)
        ...
    </pre>
    @mixin ScreenPosMixin
    @implements IMaterial
    """
    # FIXME: !!!
    # BORDER_INACCURACY = 16
    BORDER_INACCURACY = 0

    def __init__(self, x, y, width, height, screen):
        IMaterial.__init__(self, x, y, width, height)
        self.screen = screen
        self._position_info = None

    @property
    def is_inside_the_screen(self):
        return not any(self.__passed_states)

    @property
    def __passed_states(self):
        return [
            self.left_border_passed,
            self.right_border_passed,
            self.top_border_passed,
            self.bottom_border_passed,
        ]

    @property
    def position_info(self):
        labels = [("OUT" if state else "INN") for state in self.__passed_states]
        info = "L:{L} | R:{R} | T:{T} | B:{B}".format(
            L=labels[0],
            R=labels[1],
            T=labels[2],
            B=labels[3],
        )

        IS_UNDEFINED = self._position_info is None
        IS_CHANGED = self._position_info != info
        if IS_UNDEFINED or IS_CHANGED:
            self._position_info = info
            return info
        return None

    # TODO: implement by LEFT BORDER
    def left_border_passed(self, **props):
        # return self.rect.left <= self.screen.rect.left + self.BORDER_INACCURACY
        screen_rect = props.get("screen_rect", self.screen.rect)
        return self.rect.right <= screen_rect.left + self.BORDER_INACCURACY

    def right_border_passed(self, **props):
        # return self.rect.right >= self.screen.rect.right - self.BORDER_INACCURACY
        screen_rect = props.get("screen_rect", self.screen.rect)
        return self.rect.left >= screen_rect.right - self.BORDER_INACCURACY

    def top_border_passed(self, **props):
        screen_rect = props.get("screen_rect", self.screen.rect)
        # return self.rect.top <= screen_rect.top + self.BORDER_INACCURACY
        return self.rect.bottom <= screen_rect.top + self.BORDER_INACCURACY

    def bottom_border_passed(self, **props):
        screen_rect = props.get("screen_rect", self.screen.rect)
        # return self.rect.bottom >= screen_rect.bottom - self.BORDER_INACCURACY
        return self.rect.top >= screen_rect.bottom - self.BORDER_INACCURACY

    def drop_left(self):
        self.rect.x = 0

    def drop_right(self):
        self.rect.x = self.screen.width
