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

    DEFAULT_TEXTURE = "game_scene/blue_2x_diffuse.png"
    from core.models import Player
    PLAYER = Player.get_global()

    def __init__(self, caption=None):
        from core.models import Platform, SuperPlatform, JetPack, Effect, ScoreBoost
        from core.types.entities import Music, Camera

        Scene.__init__(self, caption=caption)
        ITexture.__init__(self, self.DEFAULT_TEXTURE, *self.screen.rect_tuple, self.screen,
                          auto_scale=False, auto_convert=True)
        self._platforms = [
            Platform(0, -100, 128, 32, self.screen),
            Platform(100, 0, 128, 32, self.screen),
            Platform(600, 200, 128, 32, self.screen),
            Platform(1000, 300, 128, 32, self.screen),
            Platform(800, 400, 256, 32, self.screen),
            Platform(600, 600, 128, 32, self.screen),
            Platform(432, 500, 128, 32, self.screen),
            Platform(200, 600, 128, 32, self.screen),
            Platform(200, 200, 128, 32, self.screen),
            SuperPlatform(0, 600, 128, 32, self.screen),
            SuperPlatform(1100, 650, 128, 32, self.screen),
            SuperPlatform(400, -200, 128, 32, self.screen),
            Platform(600, -500, 128, 32, self.screen),
            Platform(800, -600, 128, 32, self.screen),
            Platform(300, -700, 128, 32, self.screen),
            Platform(400, -800, 128, 32, self.screen),
            SuperPlatform(100, -1000, 128, 32, self.screen),
        ]

        self._effects = [
            Effect(200, 150, 32, 32, self.screen),
            JetPack(200, 450, 32, 32, self.screen),
            ScoreBoost(1000, 600, 32, 32, self.screen),
        ]

        # TODO: Property?
        # import copy
        self._entities = [
            *self._platforms,
            *self._effects,
            self.PLAYER,
        ]
        # self._entities_copy = copy.copy(self._entities)

        self.camera = Camera(self.screen.width, self.screen.height * 2, self.screen)

        music = Music("bg_winter.mp3")
        music.set_volume(0.2)
        music.play()

    def render(self):
        self._render_background()
        self._render_entities()

    def update(self, **props):
        if self.is_player_died:
            from core.scenes import DeathScene
            self.__reset()
            self.screen.switch_to(DeathScene(caption="Game Over", next_scene=self))
        else:
            self._update_entities(grounds=self._platforms, **props)

            # info = self.PLAYER.gravity_info
            # if info:
            #     from core.modules import console
            #     console.log(info, thread=self.THREAD, flush=True)

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

    def _render_entities(self):
        # print("."*128, "RENDER", "."*128)
        for _entity in self._entities:
            self.screen.surface.blit(_entity.image, self.camera.apply(_entity))
            # _entity.render()
            # print(_entity.image)

    def _update_entities(self, **props):
        for _entity in self._entities:
            _entity.update(**props)

        self.camera.update(self.PLAYER)

    def __reset(self):
        # FIXME:
        print("RESET")
        import copy
        from core.models import Player
        Player._reset()
        self.PLAYER = Player.get_global()
        self._entities[-1] = self.PLAYER
        # self._entities = self._entities_copy
        # self._entities[-1] = self.PLAYER
        # self._entities_copy = copy.copy(self._entities)
        # self.PLAYER = self._entities[-1]
