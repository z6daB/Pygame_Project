import pygame
from settings import *
class Interface:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.hp_value = 100

    def draw_hp(self):
        pygame.draw.rect(self.display, (255, 0, 0), (20, 20, HEALTH_WIDTH * self.hp_value, HEALTH_HEIGHT))