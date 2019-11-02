import abc


# TODO: Screen -> Scene


class IRender(abc.ABC):
    from core.types.entities.screen import Screen

    def __init__(self, screen: Screen):
        self.screen = screen

    @abc.abstractmethod
    def render(self):
        pass
