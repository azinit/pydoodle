"""
Список часто используемых констант
"""


class ScreenSize:
    """
    Query of common used screen sizes
    """
    SVGA = (800, 600)
    WXGA = (1280, 720)
    WXGA_PLUS = (1440, 900)
    FULL_HD = (1920, 1080)


class Colors:
    """
    Most-used colors in development in RGB format
    https://www.rapidtables.com/web/color/RGB_Color.html
    http://www.antula.ru/colour-rgb.htm
    https://www.google.com/search?q=cmyk&sxsrf=ACYBGNSIolPAI9aHVDlaOBbpA-Uqiy-xLQ:1572118163691&source=lnms&tbm=isch&sa=X&ved=0ahUKEwid-cPF1LrlAhUKxqYKHbDzBUIQ_AUIEigB&biw=1920&bih=975
    """
    # TODO: Import other's implementations ???

    # DARK_SHADES https://www.google.com/search?q=shades+of+black+names&sxsrf=ACYBGNSy4cqwTxRSqVGuoRdTT6GGEa7R2A:1572816223479&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjNrrCC_c7lAhUR06YKHQM2BRoQ_AUIEigB&biw=1920&bih=945#imgrc=Lj3sl4iCpOPvyM:
    # TODO: Implement!
    D_JET = (21, 21, 21)
    D_RAVEN = (57, 57, 57)
    D_ASHER = (92, 92, 92)
    D_STONE = (120, 120, 120)

    # >>> grayscale colors
    BLACK = (0, 0, 0)
    DARK = (32, 32, 32)
    GRAY = (128, 128, 128)
    LIGHT = (224, 224, 224)
    WHITE = (255, 255, 255)

    # >>> base colors
    RED = (255, 0, 0)
    ORANGE = (255, 128, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    SOFT_CYAN = (0, 128, 128)
    BLUE = (0, 0, 255)
    VIOLET = (255, 0, 255)

    @staticmethod
    def darken(color: tuple, value: int):
        return tuple(p - value for p in color)

    @staticmethod
    def lighten(color: tuple, value: int):
        return tuple(p + value for p in color)


class Direction:
    """
    Direction kinds
    """

    NORMAL = -1
    RIGHT = 0
    TOP = 1
    LEFT = 2
    BOTTOM = 3


"""
Single constants query
"""
FPS_LIMIT = 60
