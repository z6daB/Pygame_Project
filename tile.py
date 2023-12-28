import pygame

class Tile(pygame.sprite.Group):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/characters/black_character/soldier_walk1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)