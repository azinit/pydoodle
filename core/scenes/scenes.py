from core.scenes import CreditsScene, GameScene

"""
Список сцен игры на данный момент (ужасно реализовано, см. ниже)
Позже будет переделываться
"""


# Ужасно реализовал переход между сценами, завтра (03.11) буду заниматься им как раз)
# 1. Резко и без плановсти
# 2. Общая неструктурированность
# Но общая суть такая : есть объекты сцен, с помощью которых мы переключаемся на другие
# FIXME: Through props in realtime(update caption, log, ...)

def new_game():
    return GameScene(caption="Game | PyDoodle")


game_scene = new_game()
# credits_pygame = CreditsScene(label_text="powered by PyGame", next_scene=game_scene)
# credits_python = CreditsScene(label_text="Python 3.7", next_scene=credits_pygame)
# credits_smart_edu = CreditsScene(label_text="SmartEdu", next_scene=credits_python)
credits_itis = CreditsScene(label_text="ITIS", next_scene=game_scene)
