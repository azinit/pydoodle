from core.types.entities import Scene
from core.types.interfaces import ITexture


# TODO: Level ...

class GameScene(Scene, ITexture):
    """
    Игровая сцена
    @remark
    1. Дает доступ к базовому геймплею и управлению игроков
    @class GameScene
    @extends Scene
    @todo Уровневую генерацию (рандом или .map)
    """
    THREAD = "GAME_SCENE"

    DEFAULT_TEXTURE = "game_scene/base_diffuse.png"
    from core.models import Player
    PLAYER = Player.get_global()

    def __init__(self, caption=None):
        from core.models import Platform, SuperPlatform
        Scene.__init__(self, caption=caption)
        ITexture.__init__(self, self.DEFAULT_TEXTURE, *self.screen.rect_tuple, self.screen)
        self._platforms = [
            Platform(600, 200, 128, 32, self.screen),
            Platform(1000, 300, 128, 32, self.screen),
            Platform(800, 400, 256, 32, self.screen),
            Platform(600, 600, 128, 32, self.screen),
            Platform(432, 500, 128, 32, self.screen),
            Platform(200, 600, 128, 32, self.screen),
            Platform(200, 200, 128, 32, self.screen),
            SuperPlatform(0, 600, 128, 32, self.screen),
            SuperPlatform(1000, 650, 128, 32, self.screen),
        ]

        from core.types.entities import Music
        music = Music("bg_winter.mp3")
        music.set_volume(0.2)
        music.play()

    def render(self):
        self._render_background()
        self.__render_platforms()
        self.PLAYER.render()

    def update(self, **props):
        if self.is_player_died:
            from core.scenes import DeathScene
            self.__reset()
            self.screen.switch_to(DeathScene(caption="Game Over", next_scene=self))
        else:
            self.__update_platforms()
            self.PLAYER.update(grounds=self._platforms, **props)
            info = self.PLAYER.gravity_info
            if info:
                from core.modules import console
                console.log(info, thread=self.THREAD, flush=True)

    @property
    def is_player_died(self):
        return self.PLAYER.bottom_border_passed

    def handle_events(self, events):
        from pygame import (
            KEYDOWN,
            K_z
        )

        for e in events:
            if e.type == KEYDOWN and e.key == K_z:
                self.__reset()

    def _render_background(self):
        # ITexture.render(self)
        from core.consts import Colors
        self.surface.fill(Colors.DARK)

    def __render_platforms(self):
        for _platform in self._platforms:
            _platform.render()

    def __update_platforms(self):
        for _platform in self._platforms:
            _platform.update()

    def __reset(self):
        from core.models import Player
        Player._reset()
        self.PLAYER = Player.get_global()
