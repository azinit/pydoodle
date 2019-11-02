"""

TODO LIST
    Dependencies (Screen, Scene, IRender, ...)
    Update/Handle/Render - ? / ? / ? => ?
    abstractMethods -> NotIMplemented?
    GlobalSessionProps?
    Scenes as Singletones?
    Keys from pygame (global consts)
    Console.log -> depend on abstract class log() with thread setup
"""


def main():
    from core.types.entities import GameSession
    # >>> init game components: display, clock, ...
    game = GameSession()
    # >>> start game process
    game.run()


if __name__ == '__main__':
    main()
