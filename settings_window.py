import pygame
import sys
from button import *
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen


class Settings(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('graphics/menu/bg.jpg')
        self.display.blit(self.bg, (0, 0))

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()

    def draw(self):
        self.display.fill('white')


dict_screens['settings_window'] = Settings()
