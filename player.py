import pygame
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, invisible_sprites):
        super().__init__(groups)
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load(
            '../Pygame_Project-test/graphics/characters/black_character/soldier_walk1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -28)

        # создание переменной, отвечающей за направление
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.invisible_sprites = invisible_sprites

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

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')

        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        # проверка на столкновение с объектами
        if direction == 'horizontal':
            for sprite in self.invisible_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.invisible_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.keyboard_buttons()
        self.move(self.speed)
