import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, C_ORANGE, C_PURPLE, MENU_OPTION, C_SHADOW, C_WHITE, C_DARK_PURPLE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/MenuBG.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('asset/Menu.wav')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)  # DRAW RECTANGLE
            self.menu_text(40, "Sky", C_SHADOW, (255, 67))  # SHADOW SKY
            self.menu_text(90, "—Fighters—", C_SHADOW, ((WIN_WIDTH / 2), 115))  # SHADOW FIGHTERS
            self.menu_text(40, "Sky", C_ORANGE, (255, 62))  # SKY WORD
            self.menu_text(90, "—Fighters—", C_PURPLE, ((WIN_WIDTH / 2), 110))  # FIGHTER WORD

            for i in range(len(MENU_OPTION)):  # DRAW MENU
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_DARK_PURPLE, ((WIN_WIDTH / 2), 200 + 25 * i),
                                   font_name="Lucida Sans Typewriter")  # SELECT MENU
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i),
                                   font_name="Lucida Sans Typewriter")  # MENU
            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_name="Harlow Solid"):
        text_font: Font = pygame.font.SysFont(name=font_name, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
