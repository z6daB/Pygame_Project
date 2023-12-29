import pygame
import sys
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen
from level import Level
from change_cursor import change_cursor_to_aim


class Game:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.level = Level()

    def run(self):
        change_cursor_to_aim()
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
