import pygame
from settings import *


class Drawer:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font('graphics/menu/font.ttf', 12)
        
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