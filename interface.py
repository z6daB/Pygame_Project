import time
import pygame
from settings import *
from support import get_character
from game_screens import dict_screens, ChangeScreen


class Interface:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.hp_value = 100
        self.water_value = 100
        self.radiation_value = 0
        self.start_ticks = pygame.time.get_ticks()
        self.tick_interval = 5000

        self.count = 1

    def draw_bars(self):
        # draw bg
        pygame.draw.rect(
            self.display, (63, 64, 62), (20, 20, 200, HEALTH_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (63, 64, 62), (20, 50, WATER_WIDTH * 100, WATER_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (63, 64, 62), (20, 80, RADIATION_WIDTH * 100, RADIATION_HEIGHT)
        )

        # draw real bars
        pygame.draw.rect(
            self.display, (255, 0, 0), (20, 20, HEALTH_WIDTH * self.hp_value, HEALTH_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (0, 0, 255), (20, 50, WATER_WIDTH * self.water_value, WATER_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (42, 255, 4), (20, 80, RADIATION_WIDTH * self.radiation_value, RADIATION_HEIGHT)
        )

    def check_person(self):
        name = get_character()
        if name == 'woman':
            self.hp_value = 100
            self.water_value = 100
        elif name == 'white_man':
            self.hp_value = 100
            self.water_value = 20
        elif name == 'black_man':
            self.hp_value = 80
            self.water_value = 60

    def update(self):
        if self.count == 1:
            self.check_person()
            self.count += 1
        current_ticks = pygame.time.get_ticks()
        if self.hp_value <= 0:
            self.hp_value = 100
            ChangeScreen('dead')
        else:
            if current_ticks - self.start_ticks > self.tick_interval:
                if self.water_value > 0:
                    self.water_value -= 1
                elif self.water_value <= 0:
                    self.hp_value -= 1

                if self.radiation_value < 100:
                    self.radiation_value += 5
                elif self.radiation_value == 100:
                    self.hp_value -= 1

                self.start_ticks = current_ticks
