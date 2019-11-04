class IStateDependent:
    """
    Интерфейс "зависимой от состояния" сущности
    @remark
    Содержит поле state
    @interface IStateDependent
    """
    # DEFAULT_STATE = SimpleNamespace()
    # DEFAULT_STATE = lambda: None

    def __init__(self, initial_state=None):
        cur_attributes = dir(self)
        undefined_state = "state" not in cur_attributes
        undefined_bindings = "_bindings" not in cur_attributes

        if undefined_state and undefined_bindings:
            from types import SimpleNamespace
            self.state = initial_state or SimpleNamespace()
            # self.state = initial_state or self.DEFAULT_STATE
            self._bindings = []
        # else:
        #     # FIXME:
        #     print("STATE_PROPERTY_ALREADY_DEFINED")

    def activate_bindings(self):
        for _prop, handler, _val in self._bindings:
            if getattr(self.state, _prop) == _val:
                handler()

    def bind(self, state_property, state_handler, state_value=True):
        self._bindings.append((
            state_property,
            state_handler,
            state_value
        ))
