import pygame
from pygame import *


def main():
    from core.examples.scene_demo.core.consts import (
        DISPLAY,
        FLAGS,
        DEPTH
    )
    # >>> init
    pygame.init()
    # screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("SceneDemo")
    timer = pygame.time.Clock()
    running = True

    from core.examples.scene_demo.core.types.entities import SceneMananger
    manager = SceneMananger()

    while running:
        timer.tick(60)

        if pygame.event.get(QUIT):
            running = False
            return
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
