import pygame
from settings import *
from support import get_character
from creature import Creature
from game_screens import dict_screens, ChangeScreen


class Player(Creature):
    def __init__(self, groups, invisible_sprites, game, hp_value, water_value, radiation_value, speed, name):
        super().__init__(hp_value, groups, game)

        self.water_value = water_value
        self.radiation_value = radiation_value
        self.speed = speed
        self.name = name

        self.folder = name
        self.image = pygame.image.load(f'graphics/characters/{self.folder}/right/1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + self.rect.height // 2,
                                  self.rect.width, self.rect.height // 2)

        self.invisible_sprites = invisible_sprites

        self.start_ticks = pygame.time.get_ticks()
        self.tick_interval = 5000
        self.weapon_data = {
            'stick': {'cooldown': 500, 'damage': 15, 'radius': 20}
        }
        self.weapon = 'stick'
        self.attack_status = False

    def spawn(self, pos):
        self.rect.topleft = pos
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + self.rect.height // 2,
                                  self.rect.width, self.rect.height // 2)

    def keyboard_buttons(self):
        keys = pygame.key.get_pressed()
        # определение направления куда двигается игрок
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.attack_status = True
            self.direction.x = 0
            self.direction.y = 0
            self.attack_ticks = pygame.time.get_ticks()

    def animation(self):
        images = [
            '1.png', '2.png', '3.png', '4.png'
        ]
        if self.direction.x > 0 and self.direction.y != 0 \
                or self.direction.x == 0 and self.direction.y != 0 or self.direction.x > 0:
            self.frame += 0.2
            if self.frame > 3:
                self.frame -= 3
            self.image = pygame.image.load(
                f'graphics/characters/{self.folder}/right/{images[int(self.frame)]}').convert_alpha()

        elif self.direction.x < 0:
            self.frame += 0.2
            if self.frame > 3:
                self.frame -= 3
            self.image = pygame.image.load(
                f'graphics/characters/{self.folder}/left/{images[int(self.frame)]}').convert_alpha()
        else:
            self.image = pygame.image.load(f'graphics/characters/{self.folder}/idle.png').convert_alpha()

    def get_coords(self):
        return self.hitbox.x, self.hitbox.y

    def get_weapon_damage(self):
        total_damage = self.weapon_data[self.weapon]['damage']
        return total_damage

    def attack(self):
        self.set_damage_status()

    def delay(self):
        if self.attack_status:
            if self.attack_ticks - self.start_ticks > self.weapon_data[self.weapon]['cooldown']:
                self.attack_status = False
                print('attack')
                self.attack()
                self.start_ticks = self.attack_ticks

    def update_stats(self):
        current_ticks = pygame.time.get_ticks()
        if self.hp_value <= 0:
            self.kill()
            ChangeScreen('dead')
        else:
            if current_ticks - self.start_ticks > self.tick_interval:
                if self.water_value > 0:
                    self.water_value -= 1
                elif self.water_value <= 0:
                    self.hp_value -= 1

                if self.radiation_value < 100:
                    self.radiation_value += 5
                elif self.radiation_value == 100:
                    self.hp_value -= 1
                self.start_ticks = current_ticks

    def update(self):
        self.keyboard_buttons()
        self.delay()
        self.move(self.speed)
        self.animation()
        self.update_stats()

