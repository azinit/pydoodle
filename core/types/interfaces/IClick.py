from core.types.interfaces import IStateDependent


class IClick(IStateDependent):
    def __init__(self):
        super().__init__()
        self.state.on_click = False
        self.state.before_click = None
        self.bind("on_click", self.on_click)

    def on_click(self):
        raise NotImplementedError
