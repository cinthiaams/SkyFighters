import pygame

from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0],MENU_OPTION[1], MENU_OPTION[2]]: # NEW GAME 1P or 2P
                player_score = [0, 0] #Score P1 e P2
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[4]: # EXIT
                pygame.quit()  # close window
                quit()  # end pygame
            else:
                pass