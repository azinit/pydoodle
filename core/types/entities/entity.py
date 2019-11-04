from core.types.interfaces import (
    IMaterial,
    IRender,
    IUpdate,
    IStateDependent
)


# FIXME: @extends pygame.sprite???

class Entity(IMaterial, IRender, IUpdate, IStateDependent):
    """
    Класс для обозначения обрабатываемой и отображаемой сущности
    @remark
    В основном реализует статические свойства и поведения, без взаимодействия
    @class Entity
    @implements IMaterial
    @implements IRender
    @implements IUpdate
    @implements IStateDependent
    """

    def __init__(self, x, y, width, height, screen, initial_state=None):
        IMaterial.__init__(self, x, y, width, height)
        IStateDependent.__init__(self, initial_state)
        IRender.__init__(self, screen)

    def update(self, **props):
        """ Update state from old state """
        # props = {"keys": ..., "mouse": ..., ... ...}
        raise NotImplementedError

    def render(self):
        """ Dependent on state """
        raise NotImplementedError
