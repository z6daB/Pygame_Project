import pygame


class Item:
    def __init__(self):
        self.items = ['wood', 'iron', 'kumquat', 'gasmask', 'medicinal_substances']

        self.images = [
            pygame.image.load('graphics/items/wood.png'),
            pygame.image.load('graphics/items/iron.png'),
            pygame.image.load('graphics/items/kumquat.png'),
            pygame.image.load('graphics/items/gasmask.png'),
            pygame.image.load('graphics/items/medicinal_substances.png')
        ]

        self.items_crafter = ['pill_health', 'gasmaskAll', 'pill_water', 'glock', 'ak47', 'bullet']
        self.items_crafter_names = ['Здоровье', 'Противогаз', 'Для воды', 'Пистолет', 'Автомат', 'Пули']

        self.images_crafter = [
            pygame.image.load('graphics/items_crafter/pill_health.png'),
            pygame.image.load('graphics/items_crafter/gasmaskAll.png'),
            pygame.image.load('graphics/items_crafter/pill_water.png'),
            pygame.image.load('graphics/items_crafter/glock.png'),
            pygame.image.load('graphics/items_crafter/ak47.png'),
            pygame.image.load('graphics/items_crafter/bullet.png')
        ]

        self.formula_craft = {
            'pill_health': [['medicinal_substances', 6]],
            'gasmaskAll': [['iron', 1], ['gasmask', 1]],
            'pill_water': [['kumquat', 5]],
            'glock': [['iron', 8]],
            'ak47': [['iron', 13], ['wood', 7]],
            'bullet': [['iron', 3], ['wood', 2]]
        }
