import time
import pygame
from settings import *
from support import get_character
from game_screens import dict_screens, ChangeScreen
from drawer import Drawer

class Interface:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.hp_value = 100
        self.water_value = 100
        self.radiation_value = 0
        self.memories_value = 4
        self.cnt_bullet = 15
        self.cnt_bullet_max = 30
        self.start_ticks = pygame.time.get_ticks()
        self.tick_interval = 5000
        self.minimap = pygame.image.load('map/minimap.png').convert()
        self.drawer = Drawer()
        self.count = 1
    
    def draw_bars(self):
        # draw bg
        pygame.draw.rect(
            self.display, (63, 64, 62), (20, 600, 200, HEALTH_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (63, 64, 62), (20, 630, WATER_WIDTH * 100, WATER_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (63, 64, 62), (20, 660, RADIATION_WIDTH * 100, RADIATION_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (63, 64, 62), (400, 45, 500, 55)
        )

        # draw real bars
        pygame.draw.rect(
            self.display, (255, 0, 0), (20, 600, HEALTH_WIDTH * self.hp_value, HEALTH_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (0, 0, 255), (20, 630, WATER_WIDTH * self.water_value, WATER_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (42, 255, 4), (20, 660, RADIATION_WIDTH * self.radiation_value, RADIATION_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (255, 222, 0), (400, 45, 100 * self.memories_value, 55)
        )
        #count
        self.drawer.drawer_text(12, f'{self.hp_value} / 100', 'White', (75, 605))
        self.drawer.drawer_text(12, f'{self.water_value} / 100', 'White', (75, 635))
        self.drawer.drawer_text(12, f'{self.radiation_value} / 100', 'White', (75, 665))
        self.drawer.drawer_text(24, f'{self.memories_value} / 5', 'White', (575, 60))
        
        # minimap
        self.display.blit(self.minimap, (2, 2))
        pygame.draw.rect(self.display, (255, 255, 255), (0, 0, 260, 260), 2)
        
        # inventory
        pygame.draw.circle(self.display, (131, 131, 89), (WINDOW_WIDTH-60, 60), 40)
        self.inventory = pygame.image.load('map/inventory.png')
        self.display.blit(self.inventory, (WINDOW_WIDTH-92, 25))
        
        # weapon
        pygame.draw.rect(self.display, (131, 131, 89), (WINDOW_WIDTH - 250, WINDOW_HEIGHT - 120, 256, 128))
        self.weapon = pygame.image.load('graphics/weapons/stick.png')
        self.display.blit(self.weapon, (WINDOW_WIDTH - 250, WINDOW_HEIGHT - 115))
        self.drawer.drawer_text(15, f'{self.cnt_bullet} / {self.cnt_bullet_max}', 'White', (WINDOW_WIDTH - 230, WINDOW_HEIGHT - 115))

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