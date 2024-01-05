import pygame


class Zombie(pygame.sprite.Sprite):
    def __init__(self, pos, groups, invisible_sprites):
        super().__init__(groups)
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load('graphics/zombie/zombie_idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -28)

        self.direction = pygame.math.Vector2()
        self.speed = 2

        self.invisible_sprites = invisible_sprites

    def move(self, speed):
        self.hitbox.x += speed
        self.hitbox.y += speed
        self.rect.center = self.hitbox.center

    def update(self):
        self.move(self.speed)
