class IStateDependent:
    """
    Интерфейс "зависимой от состояния" сущности
    @remark
    Содержит поле state
    @interface IStateDependent
    """
    from types import SimpleNamespace
    DEFAULT_STATE = SimpleNamespace()

    def __init__(self, initial_state=None):
        self.state = initial_state or self.DEFAULT_STATE

    # TODO: State operations
