import pygame


class Creature(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.display = pygame.display.get_surface()
        self.direction = pygame.math.Vector2()

        self.frame = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        # self.person_position.x += self.direction.x * speed
        self.collision('horizontal')

        self.hitbox.y += self.direction.y * speed
        # self.person_position.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.bottom = self.hitbox.bottom
        self.rect.left = self.hitbox.left

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
