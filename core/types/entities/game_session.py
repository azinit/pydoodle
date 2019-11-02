# TODO: Singletone
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

# TODO PLAYER -> GameSssion?

import pygame
from core.modules import *


class GameSession(object):
    """
    Game substance
    """
    from core.types.entities import Screen
    THREAD = "GAME"
    FPS_LIMIT = 60
    SCREEN = Screen.get_global()

    # PLAYER =

    def __init__(self):
        """ Init components """
        from core.scenes import CreditsScene

        pygame.init()  # >>> init lib
        self.clock = pygame.time.Clock()  # >>> init clock
        self.is_running = True  # >>> init gameloop
        self.SCREEN.switch_to(CreditsScene(
            caption="Credits | PyDoodle"
        ))

    def run(self):
        """ Start gameloop """
        while self.is_running:
            self.__handle_events()
            if not self.is_running:
                return
            self.__update_game_elements()
            self.__render()
        self.__quit()

    def __handle_events(self):
        """ Poll and handle events """
        if pygame.event.get(pygame.QUIT):
            # TODO: Thread correct implementation
            self.is_running = False
            console.log("Game finished by user", thread=GameSession.THREAD)

        events = pygame.event.get()
        self.SCREEN.scene.handle_events(events)

    def __update_game_elements(self):
        """ Update states/attributes of game elements """
        keys = pygame.key.get_pressed()
        # click = pygame.click.get_pressed()
        # l = pygame.mouse.get_cursor()
        # print(l)
        self.SCREEN.scene.update(keys=keys)

    def __render(self):
        """ Draw and show surface """
        # TODO: Implement through render_objects[]?
        # blit vs update: https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip
        self.SCREEN.scene.render()
        pygame.display.update()
        # >>> FPS tick
        self.clock.tick(GameSession.FPS_LIMIT)

    def __quit(self):
        pygame.quit()
