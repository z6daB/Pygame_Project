import pygame
from support import get_character

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, invisible_sprites):
        super().__init__(groups)
        self.display = pygame.display.get_surface()
        self.folder = 'black_man'
        self.image = pygame.image.load(
            'graphics/characters/' + self.folder + '/right/1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -28)
        # создание переменной, отвечающей за направление
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.frame = 0

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

    def animation(self):
        if self.direction.x > 0 and self.direction.y != 0 \
                or self.direction.x == 0 and self.direction.y != 0 or self.direction.x > 0:
            self.frame += 0.2
            if self.frame > 3:
                self.frame -= 3
            images = [
                '1.png', '2.png', '3.png', '4.png'
            ]
            self.image = pygame.image.load(
                'graphics/characters/' + self.folder + '/right/' + images[int(self.frame)]).convert_alpha()
        elif self.direction.x < 0:
            self.frame += 0.2
            if self.frame > 3:
                self.frame -= 3
            images = [
                '1.png', '2.png', '3.png', '4.png'
            ]
            self.image = pygame.image.load(
                'graphics/characters/' + self.folder + '/left/' + images[int(self.frame)]).convert_alpha()
        else:
            self.image = pygame.image.load(
                'graphics/characters/' + self.folder + '/idle.png').convert_alpha()

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
