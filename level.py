import pygame
from settings import *
from player import Player


class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()
        # sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.invisible_sprites = pygame.sprite.Group()

        self.create_player()

    def create_player(self):
        Player((100, 100), self.visible_sprites)

    def run(self):
        self.visible_sprites.draw(self.display)
        self.visible_sprites.update()
