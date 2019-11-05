from core.types.interfaces import ITexture, IStateDependent, IUpdate


class IPureSprite(ITexture, IUpdate, IStateDependent):

    def __init__(self, texture_path, frames, x, y, width, height, screen, **props):
        ITexture.__init__(self, texture_path, x, y, width, height, screen, auto_load=False)
        IStateDependent.__init__(self)
        IUpdate.__init__(self)

        self._frames = frames
        self._frames_iter = props.get("fr_iter", 16)
        self.state.frame_val = 0

    def update(self, **props):
        self.image = self._frames[self.current_frame_num]
        if self.is_end_of_animation:
            self.state.frame_val = 0
        else:
            self.state.frame_val += 1

    @property
    def _frames_amount(self):
        return len(self._frames)

    @property
    def current_frame_num(self):
        return self.state.frame_val // self._frames_iter

    @property
    def is_end_of_animation(self):
        return self.state.frame_val == self._frames_amount * self._frames_iter - 1

