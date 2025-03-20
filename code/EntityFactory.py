import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case'Level3Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level4Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level4Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level4Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level5Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level5Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level5Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'GameOverLevel1Bg':
                return [Background('GameOverLevel1Bg', (0, 0))]
            case 'GameOverLevel2Bg':
                return [Background('GameOverLevel2Bg', (0, 0))]
            case 'GameOverLevel3Bg':
                return [Background('GameOverLevel3Bg', (0, 0))]
            case 'GameOverLevel4Bg':
                return [Background('GameOverLevel4Bg', (0, 0))]
            case 'GameOverLevel5Bg':
                return [Background('GameOverLevel5Bg', (0, 0))]
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
