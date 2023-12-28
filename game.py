import pygame
import sys
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen
from level import Level


class Game:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.level = Level()

    def run(self):
        self.event_loop()
        self.draw()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def draw(self):
        self.display.fill('white')
        self.level.run()


dict_screens['game'] = Game()
