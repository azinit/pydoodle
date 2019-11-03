from core.examples.scene_demo.core.types.entities import Scene
from core.examples.scene_demo.core.consts import (
    levels
)


class GameScene(Scene):
    def __init__(self, levelno):
        from core.examples.scene_demo.core.models import (
            Player,
            Enemy,
            ExitBlock,
            Platform
        )
        from core.examples.scene_demo.core.types.entities import (
            Camera,
            complex_camera
        )

        import pygame
        from pygame import (
            Surface,
            Color,
        )

        super(GameScene, self).__init__()
        self.bg = Surface((32, 32))
        self.bg.convert()
        self.bg.fill(Color("#0094FF"))
        up = left = right = False
        self.entities = pygame.sprite.Group()
        self.player = Player(5, 40)
        self.player.scene = self
        self.platforms = []

        self.levelno = levelno

        levelinfo = levels[levelno]
        self.enemies = [Enemy(*pos) for pos in levelinfo['enemies']]

        level = levelinfo['level']
        total_level_width = len(level[0]) * 32
        total_level_height = len(level) * 32

        # build the level
        x = 0
        y = 0
        for row in level:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    self.platforms.append(p)
                    self.entities.add(p)
                if col == "E":
                    e = ExitBlock(x, y)
                    self.platforms.append(e)
                    self.entities.add(e)
                x += 32
            y += 32
            x = 0

        self.camera = Camera(complex_camera, total_level_width, total_level_height)
        self.entities.add(self.player)
        for e in self.enemies:
            self.entities.add(e)

    def render(self, screen):
        for y in range(20):
            for x in range(25):
                screen.blit(self.bg, (x * 32, y * 32))

        for e in self.entities:
            screen.blit(e.image, self.camera.apply(e))

    def update(self):
        import pygame
        from pygame import (
            K_UP,
            K_LEFT,
            K_RIGHT,
        )

        pressed = pygame.key.get_pressed()
        up, left, right = [pressed[key] for key in (K_UP, K_LEFT, K_RIGHT)]
        self.player.update(up, left, right, self.platforms)

        for e in self.enemies:
            e.update(self.platforms)

        self.camera.update(self.player)

    def exit(self):
        from core.examples.scene_demo.core.scenes import CustomScene

        if self.levelno + 1 in levels:
            self.manager.go_to(GameScene(self.levelno + 1))
        else:
            self.manager.go_to(CustomScene("You win!"))

    def die(self):
        from core.examples.scene_demo.core.scenes import CustomScene

        self.manager.go_to(CustomScene("You lose!"))

    def handle_events(self, events):
        from core.examples.scene_demo.core.scenes import TitleScene
        from pygame import (
            KEYDOWN,
            K_ESCAPE,
        )

        for e in events:
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                self.manager.go_to(TitleScene())
