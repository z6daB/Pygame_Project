import pygame
from creature import Creature
from settings import *
from support import get_stats


class Zombie(Creature):
    def __init__(self, pos, groups, invisible_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/zombie/zombie_idle.png').convert_alpha()
        self.sprite_type = 'zombie'

        self.status = 'stop'
        self.attack_status = False

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + self.rect.height // 2,
                                  self.rect.width, self.rect.height // 2)
        self.invisible_sprites = invisible_sprites

        self.visibility_radius = 250
        self.damage_radius = 10

        self.speed = 6

        self.start_ticks = pygame.time.get_ticks()
        self.tick_interval = 5000

        self.count = 1

        self.stats = black_man
        self.reset_stats = black_man_reset
        self.dict_name = self.stats['name']

    def get_player_lenght_direction(self, player):
        zombie_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        lenght = (player_vec - zombie_vec).magnitude()
        if lenght > 0:
            direction = (player_vec - zombie_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        return lenght, direction

    def get_status(self, player):
        length = self.get_player_lenght_direction(player)[0]
        if length <= self.damage_radius:
            self.status = 'damage'
            self.attack_status = True
        elif length <= self.visibility_radius:
            self.status = 'move'
            self.attack_status = False
        else:
            self.status = 'stop'
            self.attack_status = False

    def actions(self, player):
        if self.status == 'move':
            self.direction = self.get_player_lenght_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animation(self):
        images = [
            '1.png', '2.png', '3.png', '4.png'
        ]
        if self.status == 'move':
            if self.direction.x > 0 and self.direction.y != 0 or self.direction.x == 0 \
                    and self.direction.y != 0 or self.direction.x > 0:
                self.frame += 0.2
                if self.frame > 3:
                    self.frame -= 3
                self.image = pygame.image.load(f'graphics/zombie/right/{images[int(self.frame)]}').convert_alpha()
            elif self.direction.x < 0:
                self.frame += 0.2
                if self.frame > 3:
                    self.frame -= 3
                self.image = pygame.image.load(f'graphics/zombie/left/{images[int(self.frame)]}').convert_alpha()

        elif self.status == 'damage':
            if self.attack_status is True:
                self.frame += 0.2
                if self.frame > 3:
                    self.frame -= 3
                self.image = pygame.image.load(f'graphics/zombie/attack/{images[int(self.frame)]}').convert_alpha()

        elif self.status == 'stop':
            self.image = pygame.image.load('graphics/zombie/zombie_idle.png').convert_alpha()

    def attack(self):
        if self.stats['hp_value'] > 0:
            self.stats['hp_value'] -= 50

        print(self.stats)
        print('damage')

    def delay(self):
        attack_ticks = pygame.time.get_ticks()
        if attack_ticks - self.start_ticks > self.tick_interval:
            if self.attack_status and self.status == 'damage':
                self.attack()
                self.start_ticks = attack_ticks

    def update_stats(self):
        self.stats = get_stats()
        if self.stats == 'black_man':
            self.stats = black_man
            if self.stats['hp_value'] > 0:
                self.stats = black_man
            else:
                self.stats = black_man_reset.copy()
            self.reset_stats = black_man_reset.copy()
        elif self.stats == 'white_man':
            self.stats = white_man
            if self.stats['hp_value'] > 0:
                self.stats = white_man
            else:
                self.stats = white_man_reset.copy()
            self.reset_stats = white_man_reset.copy()
        else:
            self.stats = woman
            if self.stats['hp_value'] > 0:
                self.stats = woman
            else:
                self.stats = woman_reset.copy()
            self.reset_stats = woman_reset.copy()

    def update(self):
        self.update_stats()
        self.move(self.speed)
        self.animation()
        self.delay()

    def zombie_update(self, player):
        self.get_status(player)
        self.actions(player)
