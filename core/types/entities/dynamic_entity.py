from core.types.entities import Entity
from core.mixins import ScreenPosMixin


class DynamicEntity(Entity, ScreenPosMixin):
    """
    Класс динамической сущности
    @remark
    Реализует базовые динамические параметры и поведение (дин. положение относительно экрана)
    @class DynamicEntity
    @extends Entity
    @mixin ScreenPosMixin
    @todo взаимодействие с другими сущностями через события и DynamicEntity#interact_with
    """
    def __init__(self, x, y, width, height, screen, initial_state=None):
        # Entity
        Entity.__init__(self, x, y, width, height, screen, initial_state=initial_state)
        ScreenPosMixin.__init__(self, x, y, width, height, screen)
        # print(">>>", self.BORDER_INACCURACY)
        # print(">>>", self.bottom_border_passed)
        # print(">>>", self._position_info)

    # TODO: !!!
    # @abstractmethod
    # def interact_with(self, another):
    #     """
    #     Change self.state and another state, in depend of action
    #
    #     # Examples
    #     i_w(Monster, Player): Monster HITS Player
    #     i_w(Player, Monster): Player HITS Monster
    #
    #
    #     :param self: who ->
    #     :param another: -> whom
    #     """
    #     pass
