from core.types.interfaces import IStateDependent


class IGround(IStateDependent):
    def __init__(self):
        super().__init__()
        self.state.on_landed = False
        # self.bind("on_landed", self.on_landed)

    def on_landed(self):
        raise NotImplementedError
