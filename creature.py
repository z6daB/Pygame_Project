import pygame


class Creature(pygame.sprite.Sprite):
    def __init__(self, hp_value, groups, game):
        super().__init__(groups)
        self.display = pygame.display.get_surface()
        self.direction = pygame.math.Vector2()
        self.game = game
        self.hp_value = hp_value
        self.frame = 0
        self.possibility_of_taking_damage = False

    def get_damage(self, damage):
        self.hp_value -= damage

    def set_damage_status(self):
        self.possibility_of_taking_damage = not(self.possibility_of_taking_damage)

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
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
