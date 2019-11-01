import abc


class IUpdate(abc.ABC):
    @abc.abstractmethod
    def update(self, **props):
        pass
