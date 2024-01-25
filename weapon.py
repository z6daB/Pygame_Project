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

