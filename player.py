import pygame
from settings import *
from support import get_character
from creature import Creature
from game_screens import dict_screens, ChangeScreen
from weapon import Weapon, Bullet
from random import choices, random


class Player(Creature):
    def __init__(self, groups, invisible_sprites, game, having_gun, having_handgun, having_stick, hp_value, water_value,
                 radiation_value, speed, name):
        super().__init__(hp_value, groups, game)
        self.zombies = dict_screens['game'].level.zombies

        # weapon
        self.weapon = Weapon()
        self.weapon_data = self.weapon.weapon_data
        self.weapon_items = self.weapon.weapon_items
        self.weapon_index = 2
        self.weapon_item = self.weapon_items[self.weapon_index]
        self.having_gun = having_gun
        self.having_handgun = having_handgun
        self.having_stick = having_stick

        self.weapon_have = [
            ['gun', 0, 0, self.having_gun], ['handgun', 0, 0, self.having_handgun],
            ['stick', 0, 0, self.having_stick]
        ]

        self.item_have = [
            ['wood', 0], ['iron', 0], ['kumquat', 0], ['gasmask', 0], ['medicinal_substances', 0]
        ]

        self.bullets_have = 0

        # stats
        self.water_value = water_value
        self.radiation_value = radiation_value
        self.speed = speed
        self.name = name
        self.memories_value = 0

        self.folder = name
        self.image = pygame.image.load(f'graphics/characters/{self.folder}/right/1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + self.rect.height // 2,
                                  self.rect.width, self.rect.height // 2)

        self.invisible_sprites = invisible_sprites

        self.start_ticks = pygame.time.get_ticks()
        self.tick_interval = 5000
        self.attack_status = False
        self.shoot_status = False
        self.search_status = False

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

        if pygame.mouse.get_pressed()[0]:
            self.shoot_status = True
            self.direction.x = 0
            self.direction.y = 0
            self.mouse_pos = pygame.mouse.get_pos()

        if keys[pygame.K_1]:
            if self.having_gun == 1:
                self.weapon_index = 0
        elif keys[pygame.K_2]:
            if self.having_handgun == 1:
                self.weapon_index = 1
        elif keys[pygame.K_3]:
            if self.having_stick == 1:
                self.weapon_index = 2

        if keys[pygame.K_f]:
            self.search_status = True
            self.search()

        if keys[pygame.K_r]:
            self.recharge()

    def recharge(self):
        if self.weapon_item == 'handgun':
            for i in range(len(self.weapon_have)):
                if self.weapon_have[i][0] == 'handgun':
                    if self.bullets_have >= 15 - self.weapon_have[i][1]:
                        self.bullets_have -= (15 - self.weapon_have[i][1])
                        self.weapon_have[i][1] = 15
                    else:
                        self.weapon_have[i][1] = self.bullets_have + self.weapon_have[i][1]
                        self.bullets_have = 0
                    self.weapon_have[i][2] = self.bullets_have
        elif self.weapon_item == 'gun':
            for i in range(len(self.weapon_have)):
                if self.weapon_have[i][0] == 'gun':
                    if self.bullets_have >= 30 - self.weapon_have[i][1]:
                        self.bullets_have -= (30 - self.weapon_have[i][1])
                        self.weapon_have[i][1] = 30
                    else:
                        self.weapon_have[i][1] = self.bullets_have + self.weapon_have[i][1]
                        self.bullets_have = 0
                    self.weapon_have[i][2] = self.bullets_have

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

    def attack(self):
        weapon_radius = self.weapon_data[self.weapon_item]['radius']
        zombie = dict_screens['game'].level.get_nearest_object(self, 'zombie', weapon_radius)
        if zombie:
            zombie[1].get_damage(self.weapon_data[self.weapon_item]['damage'])

    def delay(self):
        if self.weapon_item == 'stick':
            if self.attack_status:
                if self.attack_ticks - self.start_ticks > self.weapon_data[self.weapon_item]['cooldown']:
                    self.attack_status = False
                    self.attack()
                    self.start_ticks = self.attack_ticks
        else:
            # if self.shoot_status:
            #     self.shoot_status = False
            self.shoot()

    def shoot(self):
        bullet = Bullet(self.hitbox.center, pygame.mouse.get_pos())

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

    def update_weapon_item(self):
        self.weapon_item = self.weapon_items[self.weapon_index]

    def search(self):
        search_item = dict_screens['game'].level.get_nearest_object(self, 'item', 100)
        if self.search_status:
            self.search_status = False
            if search_item:
                search_item[1].interact()
                self.adding_items()

    def adding_items(self):
        num = random()
        if 1 - num <= 0.07:
            self.memories_value += 1
        items = choices(self.item_have, k=3)
        for item in items:
            item[1] += 1
            print(item)

    def check_memories(self):
        if self.memories_value == 5:
            ChangeScreen('final')

    def update(self):
        self.keyboard_buttons()
        self.delay()
        self.move(self.speed)
        self.animation()
        self.update_stats()
        self.update_weapon_item()
        self.search()
        self.check_memories()
