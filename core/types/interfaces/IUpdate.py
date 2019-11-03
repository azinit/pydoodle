class IUpdate:
    """
    Интерфейс "обновляемой" сущности
    @remark
    Содержит метод update(**props)
    В **props указываем данные (keys, mouse, ...) для обработки и обновления
    @interface IUpdate
    """
    def update(self, **props):
        # TODO: key, data, ... unpacking?
        raise NotImplementedError
