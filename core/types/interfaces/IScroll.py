from core.types.interfaces import IStateDependent


class IScroll(IStateDependent):
    DEFAULT_SCROLL_VAL = 0
    DEFAULT_SCROLL_SPEED = 1

    def __init__(self):
        IStateDependent.__init__(self)
        self.reset_scroll_state()
        self.bind("on_scroll_up", self.on_scroll_up)

    def on_scroll_up(self, **props):
        raise NotImplementedError

    def reset_scroll_state(self):
        self.state.on_scroll_up = False
        self.state.scroll_val = self.DEFAULT_SCROLL_VAL
        self.state.scroll_speed = self.DEFAULT_SCROLL_SPEED
