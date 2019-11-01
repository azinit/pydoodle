import abc


class IStateDependent(abc.ABC):
    DEFAULT_STATE = {}

    def __init__(self, initial_state=None):
        self.state = initial_state or self.DEFAULT_STATE

    # TODO: State operations
