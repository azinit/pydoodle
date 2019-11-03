class IStateDependent:
    """
    Интерфейс "зависимой от состояния" сущности
    @remark
    Содержит поле state
    @interface IStateDependent
    """
    DEFAULT_STATE = {}

    def __init__(self, initial_state=None):
        self.state = initial_state or self.DEFAULT_STATE

    # TODO: State operations
