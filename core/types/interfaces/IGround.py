from core.types.interfaces import IStateDependent, IMaterial


class IGround(IMaterial, IStateDependent):
    DEFAULT_INERTIA_VAL = 4

    def __init__(self, x, y, width, height):
        IMaterial.__init__(self, x, y, width, height)
        IStateDependent.__init__(self)
        self.state.on_landed = False
        self.state.inertia_val = self.DEFAULT_INERTIA_VAL
        self.bind("on_landed", self.on_landed)

    def on_landed(self):
        # print(self.state.inertia_val)
        self.rect.y += self.state.inertia_val

        if self.state.inertia_val == -self.DEFAULT_INERTIA_VAL:
            self.state.inertia_val = self.DEFAULT_INERTIA_VAL
            self.state.on_landed = False
        else:
            self.state.inertia_val -= 1
