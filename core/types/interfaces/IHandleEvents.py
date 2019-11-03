class IHandleEvents:
    """
    Интерфейс "обрабатывающей события" сущности
    @remark
    Содержит метод handle_events(events)
    @interface IHandleEvents
    """
    def handle_events(self, events):
        raise NotImplementedError
