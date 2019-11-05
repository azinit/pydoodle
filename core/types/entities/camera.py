from pygame import Rect


class Camera(object):
    def __init__(self, width, height, screen):
        self.state = Rect(0, 0, width, height)
        self.screen = screen

    def apply(self, target):
        try:
            return target.rect.move(self.state.topleft)
        except AttributeError:
            # TODO: Why?
            return map(sum, zip(target, self.state.topleft))

    def update(self, target):
        self.state = self.complex_camera(target.rect)

    def complex_camera(self, target_rect):
        # TODO: Smooth
        WIN_WIDTH, WIN_HEIGHT = self.screen.sizes
        HALF_WIDTH, HALF_HEIGHT = self.screen.half_sizes
        # HALF_WIDTH /= 1.5
        # HALF_HEIGHT /= 1.5
        # HALF_WIDTH = s

        l, t, _, _ = target_rect
        _, _, w, h = self.state
        l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h

        l = min(0, l)  # stop scrolling left
        l = max(-(self.state.width - WIN_WIDTH), l)  # stop scrolling right
        t = max(-(self.state.height - WIN_HEIGHT), t)  # stop scrolling bottom

        return Rect(l, t, w, h)
