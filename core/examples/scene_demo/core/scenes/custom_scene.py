class CustomScene(object):

    def __init__(self, text):
        import pygame
        self.text = text
        super(CustomScene, self).__init__()
        self.font = pygame.font.SysFont('Arial', 56)

    def render(self, screen):
        # ugly!
        screen.fill((0, 200, 0))
        text1 = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text1, (200, 50))

    def update(self):
        pass

    def handle_events(self, events):
        from pygame import KEYDOWN
        from core.examples.scene_demo.core.scenes import TitleScene

        for e in events:
            if e.type == KEYDOWN:
                self.manager.go_to(TitleScene())