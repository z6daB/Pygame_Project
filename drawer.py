import pygame
from settings import *
from weapon import Weapon
from item import Item
from game_screens import dict_screens, ChangeScreen


class Drawer:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font('graphics/menu/font.ttf', 12)
        self.weapon = Weapon()
        self.item = Item()

    def drawer_text(self, size_font, text, color, pos):
        self.font = pygame.font.Font('graphics/menu/font.ttf', size_font)
        self.surf_back = self.font.render(text, True, color)
        self.display.blit(self.surf_back, pos)

    def title_draw(self):
        pygame.draw.rect(self.display, (102, 102, 51), (WINDOW_WIDTH // 2 - 250, 50, 465, 50))
        self.drawer_text(30, 'Выбор Персонажа', 'Black', (WINDOW_WIDTH // 2 - 240, 60))
        
    def black_man_stat_draw(self):
        self.drawer_text(24, 'Михаил', 'White', (180, 185))
        self.drawer_text(12, 'Профессия:', 'Black', (130, 420))
        self.drawer_text(12, 'Строитель', 'White', (260, 420))
        self.drawer_text(12, 'Здоровье:', 'Black', (130, 440))
        self.drawer_text(12, '80 / 100', 'White', (265, 440))
        self.drawer_text(12, 'Запас воды:', 'Black', (130, 460))
        self.drawer_text(12, '60 / 100', 'White', (265, 460))
        self.drawer_text(12, 'Оружие:', 'Black', (130, 480))
        self.drawer_text(12, 'Пистолет', 'White', (260, 480))
        
    def woman_stat_draw(self):
        self.drawer_text(24, 'Антонина', 'White', (560, 185))
        self.drawer_text(12, 'Профессия:', 'Black', (530, 420))
        self.drawer_text(12, 'Мед.сестра', 'White', (650, 420))
        self.drawer_text(12, 'Здоровье:', 'Black', (530, 440))
        self.drawer_text(12, '100 / 100', 'White', (665, 440))
        self.drawer_text(12, 'Запас воды:', 'Black', (530, 460))
        self.drawer_text(12, '100 / 100', 'White', (665, 460))
        self.drawer_text(12, 'Оружие:', 'Black', (530, 480))
        self.drawer_text(12, 'Палка', 'White', (660, 480))
        
    def white_man_stat_draw(self):
        self.drawer_text(24, 'Васька', 'White', (980, 185))
        self.drawer_text(12, 'Профессия:', 'Black', (930, 420))
        self.drawer_text(12, 'Фермер', 'White', (1060, 420))
        self.drawer_text(12, 'Здоровье:', 'Black', (930, 440))
        self.drawer_text(12, '100 / 100', 'White', (1065, 440))
        self.drawer_text(12, 'Запас воды:', 'Black', (930, 460))
        self.drawer_text(12, '20 / 100', 'White', (1065, 460))
        self.drawer_text(12, 'Оружие:', 'Black', (930, 480))
        self.drawer_text(12, 'Пистолет', 'White', (1060, 480))
    
    def inventory_draw(self):
        self.weapon_have = dict_screens['game'].level.player.weapon_have
        self.item_have = dict_screens['game'].level.player.item_have
        self.drawer_text(28, 'Доступные Оружия', 'Black', (120, 120))
        for i in range(len(self.weapon_have) - 1, -1, -1):
            image = self.weapon.images[self.weapon.weapon_items.index(self.weapon_have[i][0])]
            self.display.blit(image, (150 + 325 * (len(self.weapon_have) - i - 1), 175))
            if self.weapon_have[i][0] != 'stick':
                self.drawer_text(16, f'{self.weapon_have[i][1]}/{self.weapon_have[i][2]}', 'Black', (150 + 325 * (len(self.weapon_have) - i - 1) + 200, 275))
        self.drawer_text(28, 'Доступные Предметы', 'Black', (120, 350))
        for i in range(len(self.item_have)):
            pygame.draw.rect(self.display, (0, 0, 0), (140 + 200 * i-7, 425-7, 150+14, 150+14), 7, 3)
            image = self.item.images[self.item.items.index(self.item_have[i][0])]
            self.display.blit(image, (140 + 200 * i, 425, 150, 150))
            self.drawer_text(18, f'{self.item_have[i][1]} шт.', 'Black', (185 + 200 * i, 600))
            
    def crafter_draw(self):
        for i in range(2):
            for j in range(3):
                image = self.item.images_crafter[i*3+j]
                self.display.blit(image, (150 + 200 * j, 180 + 230 * i, 150, 150))
                self.drawer_text(16, f'{self.item.items_crafter_names[i*3+j]}', 'Black', (150 + 200 * j, 145 + 240 * i))
        pygame.draw.rect(self.display, (102, 102, 51), (735, 90, 16, 600), 8, 10)
        
    def crafter_slot_draw(self, ind):
        self.drawer_text(20, self.item.items_crafter_names[ind], 'Black', (850, 120))
        image = self.item.images_crafter[ind]
        self.display.blit(image, (850, 200, 150, 150))
        self.drawer_text(16, 'Для крафта требуется:', 'Black', (780, 380))
        elem = self.item.formula_craft[self.item.items_crafter[ind]]
        for i in range(len(elem)):
            image = self.item.images[self.item.items.index(elem[i][0])]
            self.display.blit(image, (780+200*i, 400, 150, 150))
            self.drawer_text(16, f'{elem[i][1]}X', 'Black', (780+200*i, 555))
        