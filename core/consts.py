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
    BLUE = (0, 0, 255)
    VIOLET = (255, 0, 255)


class Direction:
    """
    Direction kinds
    """

    # TODO: UP/DOWN -> TOP/BOTTOM
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


"""
Single constants query
"""
FPS_LIMIT = 60
