import abc


class IRender(abc.ABC):
    def __init__(self, surface):
        self.surface = surface

    @abc.abstractmethod
    def render(self):
        pass
