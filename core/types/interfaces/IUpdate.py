import abc


class IUpdate(abc.ABC):
    @abc.abstractmethod
    def update(self, **props):
        # TODO: key, data, ... unpacking?
        pass
