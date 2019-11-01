# TODO: Singletone
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

import pygame
# from pygame.examples.aliens import Player
# from core.consts import *
from core.globals import *
from core.modules import console


# TODO: self.player or consts.PLAYER ???


class Game(object):
    """
    Game substance
    """
    THREAD = "GAME"
    FPS_LIMIT = 60

    def __init__(self):
        """ Init components """
        # >>> init lib
        pygame.init()
        # >>> init window (# TODO: use Display/Stage/Scene)
        # self.window = pygame.display.set_mode()
        # >>> init clock
        self.clock = pygame.time.Clock()
        # >>> init player
        # self.render_objects = []
        # >>> init gameloop
        self.is_running = True

    def run(self):
        """ Start gameloop """
        while self.is_running:
            self.__handle_events()
            self.__update_game_elements()
            self.__render()
        self.__quit()

    def __handle_events(self):
        """ Poll and handle events """
        for event in pygame.event.get():
            # >>> CASE: Quit
            if event.type == pygame.QUIT:
                # TODO: Thread correct implementation
                self.is_running = False
                console.log("Game finished by user", thread=Game.THREAD)

    # TODO: Update/Handle/Render - ? / ? / ? => ?
    def __update_game_elements(self):
        """ Update states/attributes of game elements """
        keys = pygame.key.get_pressed()

        # click = pygame.click.get_pressed()
        # l = pygame.mouse.get_cursor()
        # print(l)
        # TODO: Jump Logic
        # >>> handle keys
        PLAYER.update(keys=keys)

    # TODO: Implement through render_objects[]?
    def __render(self):
        """ Draw and show surface """
        # blit vs update: https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip

        # self.player.update()
        DISPLAY.render()
        PLAYER.render()
        pygame.display.update()
        # >>> FPS tick
        self.clock.tick(Game.FPS_LIMIT)

    def __quit(self):
        pygame.quit()
