import pygame


class Zombie(pygame.sprite.Sprite):
    def __init__(self, pos, groups, invisible_sprites):
        super().__init__(groups)
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load('graphics/zombie/zombie_idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -28)

        self.direction = pygame.math.Vector2()
        self.speed = 3

        self.invisible_sprites = invisible_sprites

    def get_distance_x(self, x):
        if self.hitbox.x - x == 200 or self.hitbox.x - x == -200:
            self.direction.x = 0
        elif self.hitbox.x - x > 0:
            self.direction.x = -1
        elif self.hitbox.x - x < 0:
            self.direction.x = 1

    def get_distance_y(self, y):
        if self.hitbox.y - y == 200 or self.hitbox.y - y == -200 or self.hitbox.y - y == 0:
            self.direction.y = 0
        elif self.hitbox.y - y > 0:
            self.direction.y = -1
        elif self.hitbox.y - y < 0:
            self.direction.y = 1

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
        pass

    def update(self):
        self.move(self.speed)
        self.animation()
