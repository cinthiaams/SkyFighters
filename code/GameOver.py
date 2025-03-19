import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, WIN_HEIGHT, C_WHITE, SCORE_POS, MENU_OPTION
from code.EntityFactory import EntityFactory


class GameOver:
    def __init__(self, window: Surface, level: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.level = level
        self.game_mode = game_mode
        self.player_score = player_score
        self.background = EntityFactory.get_entity(f'GameOver{level}Bg')[0]

    def run(self):
        pygame.mixer_music.load('asset/GameOver.wav')
        pygame.mixer_music.set_volume(0.7)
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.background.surf, dest=self.background.rect)
            self.display_text(48, "Game Over", C_WHITE, (WIN_WIDTH / 2, 50))

            if self.game_mode == MENU_OPTION[0]:
                self.display_text(30, f"Score: {self.player_score[0]}", C_WHITE, (WIN_WIDTH / 2, 100))
            else:
                self.display_text(30, f"Player 1 Score: {self.player_score[0]}", C_WHITE, (WIN_WIDTH / 2, 90))
                self.display_text(30, f"Player 2 Score: {self.player_score[1]}", C_WHITE, (WIN_WIDTH / 2, 120))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        return  # Sai da tela de Game Over

            pygame.display.flip()

    def display_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
