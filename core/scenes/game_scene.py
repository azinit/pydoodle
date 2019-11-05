from core.types.entities import Scene
from core.types.interfaces import ITexture, IScroll


# TODO: Level ...

class GameScene(Scene, ITexture, IScroll):
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
    FOOTER_MIN = 100
    BEST_SCORE = 0
    on_best_score = lambda **props: None

    def __init__(self, caption=None):
        Scene.__init__(self, caption=caption)
        ITexture.__init__(self, self.DEFAULT_TEXTURE, *self.screen.rect_tuple, self.screen,
                          auto_scale=False, auto_convert=True)
        IScroll.__init__(self)

        from core.controls import Label
        from core.consts import Colors

        self.__reset_entities()
        self._controls.extend([
            Label("BEST SCORE:", 100, 32, self.screen, color=Colors.WHITE, font_size=24),
            Label("ACTUAL SCORE:", 100, 64, self.screen, color=Colors.WHITE, font_size=24),
            Label("0", 200, 32, self.screen, color=Colors.GREEN, font_size=24),
            Label("0", 200, 64, self.screen, color=Colors.YELLOW, font_size=24),
        ])

    def __reset_entities(self):
        from core.models import Platform, SuperPlatform, JetPack, Effect, ScoreBoost
        from core.types.entities import Music

        self.score = 0

        # self.test_btn = Button(None, 100, 100, 128, 32, self.screen, text="Click me", font_size=16)
        # print(self.test_btn)

        self._platforms = [
            Platform(1100, 650, 128, 32, self.screen),
            Platform(0, 600, 128, 32, self.screen),
            Platform(200, 600, 128, 32, self.screen),
            Platform(600, 600, 128, 32, self.screen),
            Platform(432, 500, 128, 32, self.screen),
            Platform(800, 400, 256, 32, self.screen),
            Platform(1000, 300, 128, 32, self.screen),
            Platform(600, 200, 128, 32, self.screen),
            Platform(200, 200, 128, 32, self.screen),
            Platform(100, 0, 128, 32, self.screen),
        ]

        self._effects = [
            # Effect(200, 150, 32, 32, self.screen),
            # JetPack(200, 450, 32, 32, self.screen),
            # ScoreBoost(1000, 600, 32, 32, self.screen),
        ]

        # TODO: Property?
        music = Music("bg_winter.mp3")
        music.set_volume(0.2)
        # music.play()

    """
    ..............................................................................................................
    ................................................ UPDATE ......................................................
    ..............................................................................................................
    """

    def update(self, **props):
        if self.is_player_died:
            self.on_player_died()
            return

        self.PLAYER.update(
            grounds=self._platforms,
            scroll_up=self.scroll_up,
            **props
        )
        self._update__controls()
        self._update_entities(**props)
        self.activate_bindings()

    def _update_entities(self, **props):
        for entity in [*self._platforms, *self._effects]:
            entity.update()

    def __process_platforms(self):
        import random
        from core.models import Platform, SuperPlatform
        DEF_WIDTH, DEF_HEIGHT = Platform.DEFAULT_SIZES
        POS_Y_MAX = DEF_HEIGHT * 2
        POS_X_MAX = self.screen.width - DEF_WIDTH

        # >>> remove invisible (passed bottom)
        for i, _p in enumerate(self._platforms):
            if _p.bottom_border_passed():
                self._platforms.remove(_p)

        # TODO: @generator
        # TODO: class Generator or PlatformBased
        # >>> generate new
        amount = random.randint(1, 3)
        std_share = 1 / amount
        cur_share = 0
        for _ in range(amount):
            # is_super = (random.randint(0, 10) == 0)
            is_super = True

            RandomPlatform = SuperPlatform if is_super else Platform

            pos_x = random.randint(
                int(POS_X_MAX * cur_share),
                int(POS_X_MAX * (cur_share + std_share)),
            )
            pos_y = -DEF_HEIGHT - random.randint(
                int(POS_Y_MAX * cur_share),
                int(POS_Y_MAX * (cur_share + std_share)),
            )

            p = RandomPlatform(pos_x, pos_y, DEF_WIDTH, DEF_HEIGHT, self.screen)
            self._platforms.append(p)
            cur_share += std_share
        # self._platforms

    def _update__controls(self):
        # FIXME: HARDCODE
        self._controls[2].update(text=str(self.BEST_SCORE))
        self._controls[3].update(text=str(self.score))

    """
    ..............................................................................................................
    ................................................ EVENTS ......................................................
    ..............................................................................................................
    """

    def handle_events(self, events):
        from pygame import (
            KEYDOWN,
            K_z
        )

        for e in events:
            if e.type == KEYDOWN and e.key == K_z:
                self.__reset()

    """
    @event on_scroll_up
    """

    def scroll_up(self, **props):
        ground = props.get("ground")
        if ground:
            value = self.__scroll_border - ground.rect.bottom
            self.state.on_scroll_up = True
            self.state.scroll_val = value

            self.score += 1
            self.__process_platforms()

    def on_scroll_up(self, **props):
        for p in self._platforms:
            p.update(scroll_up=self.state.scroll_speed)

        if self.state.scroll_val <= self.DEFAULT_SCROLL_VAL:
            self.reset_scroll_state()
        else:
            self.state.scroll_speed += 0.5
            self.state.scroll_val -= self.state.scroll_speed

    @property
    def __scroll_border(self):
        return self.screen.rect.bottom - self.FOOTER_MIN

    """
    @event on_player_died
    """

    @property
    def is_player_died(self):
        return self.PLAYER.bottom_border_passed()

    def on_player_died(self):
        from core.scenes import DeathScene
        # >>> if score increased
        if self.score > self.BEST_SCORE:
            self.BEST_SCORE = self.score
            self.on_best_score(best_score=self.BEST_SCORE)

        # >>> reset scene
        self.__reset()
        self.screen.switch_to(DeathScene(caption="Game Over", next_scene=self))

    """
    ..............................................................................................................
    ................................................ RENDER ......................................................
    ..............................................................................................................
    """

    def render(self):
        self._render_background()
        self._render_entities()
        self._render__controls()
        self.PLAYER.render()

    def __reset(self):
        from core.models import Player
        self.PLAYER = Player.get_global(reset=True)
        self.__reset_entities()

    def _render_background(self):
        # ITexture.render(self)
        from core.consts import Colors
        self.surface.fill(Colors.DARK)
        # self.screen.draw.rect(self.surface, Colors.GRAY, (0, self.__scroll_border, self.screen.width, self.FOOTER_MIN))

    def _render_entities(self):
        for entity in [*self._platforms, *self._effects]:
            entity.render()
