import pygame
from pygame.examples.grid import WINDOW_WIDTH

# C
C_ORANGE = (255, 132, 0)
C_PURPLE = (91, 49, 142)
C_PINK = (205, 35, 122)
C_DARK_PURPLE = (62, 28, 80)
C_WHITE = (255, 255, 255)
C_SHADOW = (61, 40, 53)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'GameOverLevel1Bg': 0,
    'GameOverLevel2Bg': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 300,
    'Enemy1Shot': 20,
    'Enemy2': 300,
    'Enemy2Shot': 25

}
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'GameOverLevel1Bg': 999,
    'GameOverLevel2Bg': 999,
    'Player1': 25,
    'Player1Shot': 1,
    'Player2': 25,
    'Player2Shot': 1,
    'Enemy1': 60,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'GameOverLevel1Bg': 0,
    'GameOverLevel2Bg': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 50,
    'Enemy2': 30,
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,
    'GameOverLevel1Bg': 0,
    'GameOverLevel2Bg': 0,
    'Player1': 3,
    'Player1Shot': 5,
    'Player2': 3,
    'Player2Shot': 5,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 5
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_f}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_LEVEL = 30000
TIMEOUT_STEP = 100

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S (depends on the W)
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 85),
             'Label': (WIN_WIDTH / 2, 95),
             'Name': (WIN_WIDTH / 2, 115),
             0: (WIN_WIDTH / 2, 115),
             1: (WIN_WIDTH / 2, 135),
             2: (WIN_WIDTH / 2, 155),
             3: (WIN_WIDTH / 2, 175),
             4: (WIN_WIDTH / 2, 195),
             5: (WIN_WIDTH / 2, 215),
             6: (WIN_WIDTH / 2, 235),
             7: (WIN_WIDTH / 2, 255),
             8: (WIN_WIDTH / 2, 275),
             9: (WIN_WIDTH / 2, 295)
             }
