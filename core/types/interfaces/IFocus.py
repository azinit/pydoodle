from core.types.interfaces import IStateDependent


class IFocus(IStateDependent):
    def __init__(self):
        super().__init__()
        self.state.on_focus = False
        self.state.before_focus = None
        self.bind("on_focus", self.on_focus)

    def on_focus(self, **props):
        raise NotImplementedError
