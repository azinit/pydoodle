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
        from core.models import Platform
        super().__init__(caption=caption)
        self._platforms = [
            Platform(200, 100, 128, 32, self.screen),
            Platform(600, 200, 128, 32, self.screen),
            Platform(400, 300, 128, 32, self.screen),
            Platform(200, 400, 128, 32, self.screen),
            Platform(32, 500, 128, 32, self.screen),
        ]
        # import copy
        # self.PLAYER_COPY = copy.copy(self.PLAYER)

    def render(self):
        self.__render()
        self.__render_platforms()
        self.PLAYER.render()

    def update(self, **props):
        self.PLAYER.update(platforms=self._platforms, **props)
        # info = PLAYER.is_inside_the_screen
        from pygame import (
            K_LCTRL,
            K_RCTRL,
            K_z
        )

        keys = props.get("keys")

        # if keys[K_LCTRL] and keys[K_z]:
        #     self.__reset()

        info = self.PLAYER.position_info
        if info:
            from core.modules import console
            console.log(info, thread=self.THREAD)

    def handle_events(self, events):
        from pygame import (
            KEYDOWN,
            K_LCTRL,
            K_z
        )

        # PRESSED_CTRL = False
        # PRESSED_Z = False
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_z:
                    self.__reset()
        # print(PRESSED_CTRL, PRESSED_Z)
        # if PRESSED_CTRL and PRESSED_Z:
        #     print("Ctrl + Z!")

    def __render(self):
        from core.consts import Colors
        self.surface.fill(Colors.DARK)

    def __render_platforms(self):
        for _platform in self._platforms:
            _platform.render()

    def __reset(self):
        # import copy
        # FIXME:
        # self.PLAYER = self.PLAYER_COPY
        # self.PLAYER_COPY = copy.copy(self.PLAYER_COPY)
        from core.models import Player
        Player._reset()
        self.PLAYER = Player.get_global()

