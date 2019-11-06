from core.scenes import CreditsScene, GameScene, MenuScene

"""
Список сцен игры на данный момент (ужасно реализовано, см. ниже)
Позже будет переделываться
"""

# ugly!
# FIXME: Through props in realtime(update caption, log, ...)

game_scene = GameScene(caption="Game | PyDoodle")
menu_scene = MenuScene(caption="Menu | PyDoodle")
credits_pygame = CreditsScene(label_text="powered by PyGame", next_scene=menu_scene, texture="credits/pygame.png")
credits_python = CreditsScene(label_text="Python 3.7", next_scene=credits_pygame, texture="credits/python.png")
# credits_smart_edu = CreditsScene(label_text="SmartEdu", next_scene=credits_python)
credits_itis = CreditsScene(label_text="ITIS", next_scene=credits_python, texture="credits/itis.png")
