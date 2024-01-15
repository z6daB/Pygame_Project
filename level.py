import pygame
from settings import *
from player import Player
from tile import Tile
from imports import *
from zombie import Zombie
from interface import Interface


class Level:
    def __init__(self, game):
        self.display = pygame.display.get_surface()
        # sprite groups
        self.visible_sprites = CameraGroup()
        self.invisible_sprites = pygame.sprite.Group()
        self.game = game
        self.zombies = []
        self.create_map()
        self.interface = Interface(game)

    def create_map(self):
        layouts = {
            'border': import_csv('map/map_Blocked.csv'),
            'creature': import_csv('map/map_creature.csv')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'border':
                            Tile((x, y), self.invisible_sprites, 'invisible')
                        if style == 'creature':
                            if col == '0':
                                self.player_spawn = (x, y)
                            else:
                                self.zombies.append(Zombie((x, y), self.visible_sprites, self.invisible_sprites, self.game))

    def spawn_player(self, player):
        self.player = player
        self.player.spawn(self.player_spawn)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        for zombie in self.zombies:
            zombie.zombie_update(self.player)
        self.visible_sprites.update()
        self.interface.draw_bars()
        self.interface.draw_minimap()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.half_width = self.display.get_size()[0] // 2
        self.half_height = self.display.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        # загрузка карты
        self.floor = pygame.image.load('map/map.png').convert()
        self.floor_rect = self.floor.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        floor_offset = self.floor_rect.topleft - self.offset
        self.display.blit(self.floor, floor_offset)
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, offset_pos)

