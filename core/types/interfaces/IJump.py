class IJump:
    """
    Интерфейс "прыгающей" сущности
    @remark
    Содержит метод jump()
    @interface IJump
    @todo connect with mixin
    """
    def jump(self):
        raise NotImplementedError
