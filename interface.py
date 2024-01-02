import pygame
from settings import *


class Interface:
    def __init__(self):
        self.display = pygame.display.get_surface()

        self.hp_value = 100
        self.water_value = 70
        self.radiation_value = 20

    def draw_hp(self):
        pygame.draw.rect(self.display, (63, 64, 62), (20, 20, HEALTH_WIDTH * 100, HEALTH_HEIGHT))
        pygame.draw.rect(self.display, (255, 0, 0), (20, 20, HEALTH_WIDTH * self.hp_value, HEALTH_HEIGHT))

    def draw_water(self):
        pygame.draw.rect(self.display, (63, 64, 62), (20, 50, WATER_WIDTH * 100, WATER_HEIGHT))
        pygame.draw.rect(self.display, (0, 0, 255), (20, 50, WATER_WIDTH * self.water_value, WATER_HEIGHT))

    def draw_radiation(self):
        pygame.draw.rect(self.display, (63, 64, 62), (20, 80, RADIATION_WIDTH * 100, RADIATION_HEIGHT))
        pygame.draw.rect(self.display, (42, 255, 4), (20, 80, RADIATION_WIDTH * self.radiation_value, RADIATION_HEIGHT))

    def update(self):
        if self.hp_value <= 0:
            print('lose')
