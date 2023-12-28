import pygame
import sys
from button import *
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen


class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()
        # sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.invisible_sprites = pygame.sprite.Group()

    def run(self):
        pass
