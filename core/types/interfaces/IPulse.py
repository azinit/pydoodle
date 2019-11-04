from core.types.interfaces import IStateDependent, IMaterial


# TODO: OneLogic for IGround and IPulse?

class IPulse(IMaterial, IStateDependent):
    DEFAULT_PULSE_VAL = 8

    def __init__(self, x, y, width, height):
        IMaterial.__init__(self, x, y, width, height)
        IStateDependent.__init__(self)
        self.state.on_pulsed = True
        self.state.pulse_val = self.DEFAULT_PULSE_VAL
        self.bind("on_pulsed", self.on_pulsed)

    def on_pulsed(self):
        # FIXME: IMPLEMENT WITH SIZES!
        # FIXME: Speed of pulse! (Iter?)

        self.rect.x += self.state.pulse_val
        # new_rect = (
        #     self.width + self.state.pulse_val,
        #     self.height + self.state.pulse_val
        # )
        #
        # self._texture

        if self.state.pulse_val == -self.DEFAULT_PULSE_VAL:
            self.state.pulse_val = self.DEFAULT_PULSE_VAL
            # self.state.on_pulsed = False
        else:
            self.state.pulse_val -= 1
