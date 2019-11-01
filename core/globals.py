from core.consts import Screen
from core.types.entity.display import Display

# >>> init display
from core.models.player import Player

"""
Init main display singletone
"""
DISPLAY = Display(*Screen.WXGA)

"""
Init main player singletone
"""
PLAYER = Player(
    x=50,
    y=425,
    width=60,
    height=71,
    surface=DISPLAY.window
)
