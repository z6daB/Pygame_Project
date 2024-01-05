import pygame


class Zombie(pygame.sprite.Sprite):
    def __init__(self, pos, group, invisible_sprite):
        super().__init__(group)
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load('graphics/zombie/zombie_idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -28)

        self.direction = pygame.math.Vector2()
        self.speed = 0.5

    def move(self, speed):
        self.hitbox.x += speed
        self.hitbox.y += speed
        self.rect.center = self.hitbox.center

    def update(self):
        self.move(self.speed)
