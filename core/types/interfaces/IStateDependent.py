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
        self._bindings = []

    def activate_bindings(self):
        for _prop, handler in self._bindings:
            if getattr(self.state, _prop):
                handler()

    def bind(self, state_property, state_handler):
        self._bindings.append((
            state_property,
            state_handler)
        )
