import pygame.display
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen
from level import Level


class Game(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.level = Level

    def event_loop(self):
        pass

    def draw(self):
        pass


dict_screens['game'] = Game()