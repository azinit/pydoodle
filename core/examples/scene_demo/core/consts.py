WIN_WIDTH = 1120 - 320
WIN_HEIGHT = 960 - 320
# WIN_WIDTH = 1120
# WIN_HEIGHT = 960
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 0
FLAGS = 0
CAMERA_SLACK = 30

levels = {
    0: {
        'level': [
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                         E  ",
            "                            PPPPPPPPPPPPPPPP",
            "                            PPPPPPPPPPPPPPPP",
            "                            PPPPPPPPPPPPPPPP",
            "               PPPPP        PPPPPPPPPPPPPPPP",
            "                            PPPPPPPPPPPPPPPP",
            "                            PPPP           P",
            "                            PPPP           P",
            "                            PPPP     PPPPPPP",
            "                      PPPPPPPPPP     PPPPPPP",
            "                            PPPP     PPPPPPP",
            "       PPPP                 PPPP     PPPPPPP",
            "                            PPPP     PPPPPPP",
            "                            PPPP     PPPPPPP",
            "                            PPPP     PPPPPPP",
            "PPPPP                       PPPP     PPPPPPP",
            "PPP                         PPPP     PPPPPPP",
            "PPP                         PPPP     PPPPPPP",
            "PPP                         PPPP     PPPPPPP",
            "PPP         PPPPP           PPPP     PPPPPPP",
            "PPP                                     PPPP",
            "PPP                                     PPPP",
            "PPP                                     PPPP",
            "PPP                       PPPPPPPPPPPPPPPPPP",
            "PPP                       PPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP", ],
        'enemies': [(9, 38)]
    },
    1: {
        'level': [
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                            ",
            "                                         E  ",
            "                            PPPPPPPPPPPPPPPP",
            "                            PPPPPPPPPPPPPPPP",
            "                            PPPPPPPPPPPPPPPP",
            "               PPPPP        PPPPPPPPPPPPPPPP",
            "                            PPPPPPPPPPPPPPPP",
            "                            PPPP           P",
            "                            PPPP           P",
            "                            PPPP     PPPPPPP",
            "                      PPPPPPPPPP     PPPPPPP",
            "                            PPPP     PPPPPPP",
            "       PPPP                 PPPP     PPPPPPP",
            "                            PPPP     PPPPPPP",
            "                            PPPP     PPPPPPP",
            "                            PPPP     PPPPPPP",
            "PPPPP                       PPPP     PPPPPPP",
            "PPP                  PPPPPPPPPPP     PPPPPPP",
            "PPP                         PPPP     PPPPPPP",
            "PPP                         PPPP     PPPPPPP",
            "PPP             PPPPPPPP    PPPP     PPPPPPP",
            "PPP                                     PPPP",
            "PPP                                     PPPP",
            "PPP          PPPPP                      PPPP",
            "PPP          P            PPPPPPPPPPPPPPPPPP",
            "PPP          P    PPPPPPPPPPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP",
            "PPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPP", ],
        'enemies': [(9, 38), (18, 38), (15, 15)]
    }
}