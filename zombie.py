import pygame
from creature import Creature


class Zombie(Creature):
    def __init__(self, pos, groups, invisible_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/zombie/zombie_idle.png').convert_alpha()
        self.sprite_type = 'zombie'
        self.status = 'stop'
        self.atack = False

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + self.rect.height // 2,
                                  self.rect.width, self.rect.height // 2)
        self.invisible_sprites = invisible_sprites

        self.visibility_radius = 250
        self.damage_radius = 10

        self.speed = 6

    def get_player_lenght_direction(self, player):
        zombie_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        lenght = (player_vec - zombie_vec).magnitude()
        if lenght > 0:
            direction = (player_vec - zombie_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        return lenght, direction

    def get_status(self, player):
        length = self.get_player_lenght_direction(player)[0]
        if length <= self.damage_radius:
            self.status = 'damage'
            self.atack = True
        elif length <= self.visibility_radius:
            self.status = 'move'
            self.atack = False
        else:
            self.status = 'stop'
            self.atack = False

    def actions(self, player):
        if self.status == 'move':
            self.direction = self.get_player_lenght_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animation(self):
        images = [
            '1.png', '2.png', '3.png', '4.png'
        ]
        if self.status == 'move':
            if self.direction.x > 0 and self.direction.y != 0 or self.direction.x == 0 \
                    and self.direction.y != 0 or self.direction.x > 0:
                self.frame += 0.2
                if self.frame > 3:
                    self.frame -= 3
                self.image = pygame.image.load(f'graphics/zombie/right/{images[int(self.frame)]}').convert_alpha()
            elif self.direction.x < 0:
                self.frame += 0.2
                if self.frame > 3:
                    self.frame -= 3
                self.image = pygame.image.load(f'graphics/zombie/left/{images[int(self.frame)]}').convert_alpha()

        elif self.status == 'damage':
            if self.atack:
                self.frame += 0.2
                if self.frame > 3:
                    self.frame -= 3
                self.image = pygame.image.load(f'graphics/zombie/atack/{images[int(self.frame)]}').convert_alpha()

        elif self.status == 'stop':
            self.image = pygame.image.load('graphics/zombie/zombie_idle.png').convert_alpha()

    def update(self):
        self.move(self.speed)
        self.animation()

    def zombie_update(self, player):
        self.get_status(player)
        self.actions(player)
