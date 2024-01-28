import pygame


class Weapon:
    def __init__(self):
        self.weapon_data = {
            'stick': {'cooldown': 500, 'damage': 10, 'radius': 20},
            'gun': {'cooldown': 100, 'damage': 20, 'radius': 300, 'bullets': 30},
            'handgun': {'cooldown': 300, 'damage': 30, 'radius': 250, 'bullets': 15}
        }

        self.weapon_items = ['gun', 'handgun', 'stick']

        self.images = [
            pygame.image.load('graphics/weapons/ak47.png'),
            pygame.image.load('graphics/weapons/glock.png'),
            pygame.image.load('graphics/weapons/stick.png')
        ]


class Bullet:
    def __init__(self, start_cords, end_cords):
        self.display = pygame.display.get_surface()
        self.x = start_cords[0]
        self.y = start_cords[1]
        self.end_cords = end_cords
        self.image_bullet = pygame.image.load('graphics/weapons/bullet.png').convert_alpha()
        self.hitbox = self.image_bullet.get_rect()
        self.speed = 8

    def draw(self):
        self.display.blit(self.image_bullet, (self.x, self.y))
        self.update_pos()

    def get_direction(self):
        start_vec = pygame.math.Vector2((self.x, self.y))
        end_vec = pygame.math.Vector2(self.end_cords)
        direction = (end_vec - start_vec).normalize()
        return direction

    def update_pos(self):
        direction = self.get_direction()
        self.x += direction.x * self.speed
        self.y += direction.y * self.speed
        print('update')

    def update(self):
        self.draw()
        # direction = self.get_direction()
        # if direction.x == 0 and direction.y == 0:
        #     self.kill()
