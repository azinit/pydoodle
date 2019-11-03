class IMove:
    """
    Интерфейс "двигающейся" сущности
    @remark
    Содержит метод move(props)
    @interface IMove
    @todo connect with mixin
    """
    def move(self, props):
        raise NotImplementedError
