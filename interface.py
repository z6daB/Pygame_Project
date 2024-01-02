import pygame
from settings import *
class Interface:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.hp_value = 100
        self.water_value = 100
        self.radiation_value = 100

    def draw_hp(self):
        pygame.draw.rect(self.display, (255, 0, 0), (20, 20, HEALTH_WIDTH * self.hp_value, HEALTH_HEIGHT))

    def draw_water(self):
        pygame.draw.rect(self.display, (0, 0, 255), (20, 50, WATER_WIDTH * self.water_value, WATER_HEIGHT))

    def draw_radiation(self):
        pygame.draw.rect(self.display, (42, 255, 4), (20, 80, RADIATION_WIDTH * self.radiation_value, RADIATION_HEIGHT))