import pygame
import sys
from button import *
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen


class Level(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def draw(self):
        self.display.fill('black')


dict_screens['level'] = Level()
