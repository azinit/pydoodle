from core.types.interfaces import IStateDependent


class IPause(IStateDependent):
    def __init__(self):
        super().__init__()
        self.state.on_pause = False
        self.bind("on_pause", self.on_pause)

    def on_pause(self):
        raise NotImplementedError
