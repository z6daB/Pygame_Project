import pygame
from settings import *
from support import get_character
from creature import Creature


class Player(Creature):
    def __init__(self, pos, groups, invisible_sprites):
        super().__init__(groups)
        self.folder = 'black_man'
        self.image = pygame.image.load(f'graphics/characters/{self.folder}/right/1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + self.rect.height // 2,
                                  self.rect.width, self.rect.height // 2)

        self.invisible_sprites = invisible_sprites
        self.speed = 7

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

    def update(self):
        self.keyboard_buttons()
        self.move(self.speed)
        self.animation()

        name = get_character()
        if name == 'woman':
            self.folder = 'woman'
        elif name == 'white_man':
            self.folder = 'white_man'
        elif name == 'black_man':
            self.folder = 'black_man'
