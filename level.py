import pygame
from settings import *
from player import Player
from tile import Tile

class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()
        # sprite groups
        self.visible_sprites = CameraGroup()
        self.invisible_sprites = pygame.sprite.Group()

        self.create_player()

    def create_player(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.invisible_sprites])
                if col == 'p':
                    self.player = Player((100, 100), self.visible_sprites, self.invisible_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.half_width = self.display.get_size()[0] // 2
        self.half_height = self.display.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)
