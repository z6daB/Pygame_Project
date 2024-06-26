import pygame
import sys
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen
from level import Level
from change_cursor import change_cursor_to_aim
from interface import Interface


class Game:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.level = Level(self)

    def run(self):
        change_cursor_to_aim()
        self.event_loop()
        self.draw()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.level.run()


