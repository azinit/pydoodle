from abc import abstractmethod
from core.types.interfaces import *


# TODO: Or pygame.sprite???
# TODO: Interfaces for other...


class Entity(IMaterial, IRender, IUpdate, IStateDependent):
    DEFAULT_STATE = {}

    def __init__(self, x, y, width, height, surface, initial_state=None):
        IMaterial.__init__(self, x, y, width, height, surface)
        IStateDependent.__init__(self, initial_state)

    @abstractmethod
    def update(self, **props):
        """ Update state from old state """
        # props = {"keys": ..., "mouse": ..., ... ...}
        pass

    @abstractmethod
    def render(self):
        """ Dependent on state """
        pass

    @abstractmethod
    def interact_with(self, another):
        """ Change self.state and another state, in depend of action """
        pass
