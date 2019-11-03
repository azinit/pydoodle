from core.types.entities import Scene


# TODO: Level ...

class GameScene(Scene):
    """
    Игровая сцена
    @remark
    1. Дает доступ к базовому геймплею и управлению игроков
    @class GameScene
    @extends Scene
    @todo Уровневую генерацию (рандом или .map)
    """
    THREAD = "GAME_SCENE"

    from core.models import Player
    PLAYER = Player.get_global()

    def __init__(self, caption=None):
        super().__init__(caption=caption)

    def render(self):
        self.__render()
        self.PLAYER.render()

    def update(self, **props):
        self.PLAYER.update(**props)
        # info = PLAYER.is_inside_the_screen
        info = self.PLAYER.position_info
        if info:
            from core.modules import console
            console.log(info, thread=self.THREAD)

    def handle_events(self, events):
        pass

    def __render(self):
        from core.consts import Colors
        self.screen.surface.fill(Colors.DARK)
