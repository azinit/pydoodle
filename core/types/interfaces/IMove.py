import abc


class IMove(abc.ABC):
    @abc.abstractmethod
    def move(self, props):
        pass
