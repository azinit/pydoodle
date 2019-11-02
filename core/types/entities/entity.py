from core.types.interfaces import *

# TODO: Or pygame.sprite???
# TODO: Interfaces for other...


class Entity(IMaterial, IRender, IUpdate, IStateDependent):
    DEFAULT_STATE = {}

    def __init__(self, x, y, width, height, screen, initial_state=None):
        IMaterial.__init__(self, x, y, width, height)
        IStateDependent.__init__(self, initial_state)
        IRender.__init__(self, screen)

    def update(self, **props):
        """ Update state from old state """
        # props = {"keys": ..., "mouse": ..., ... ...}
        raise NotImplementedError

    def render(self):
        """ Dependent on state """
        raise NotImplementedError
