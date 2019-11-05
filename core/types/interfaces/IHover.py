from core.types.interfaces import IStateDependent


class IHover(IStateDependent):
    def __init__(self):
        IStateDependent.__init__(self)
        self.state.on_hover = False
        self.state.before_hover = None
        self.bind("on_hover", self.on_hover)

    def on_hover(self):
        raise NotImplementedError