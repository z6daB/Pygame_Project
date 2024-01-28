import time
import sys
import pygame
from settings import *
from game_screens import dict_screens, ChangeScreen
from drawer import Drawer
from button import *
from weapon import Weapon


class Interface:
    def __init__(self, game):
        self.game = game
        self.button = Button()
        self.weapon = Weapon()
        self.display = pygame.display.get_surface()
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
            self.display, (255, 0, 0), (20, 600, HEALTH_WIDTH * min(100, self.game.level.player.hp_value), HEALTH_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (0, 0, 255), (20, 630, WATER_WIDTH * min(100,self.game.level.player.water_value), WATER_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (42, 255, 4), (20, 660, RADIATION_WIDTH * min(100,self.game.level.player.radiation_value), RADIATION_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (255, 222, 0), (400, 45, 100 * self.memories_value, 55)
        )
        # count
        self.drawer.drawer_text(12, f'{min(100, self.game.level.player.hp_value)} / 100', 'White', (75, 605))
        self.drawer.drawer_text(12, f'{min(100,self.game.level.player.water_value)} / 100', 'White', (75, 635))
        self.drawer.drawer_text(12, f'{min(100,self.game.level.player.radiation_value)} / 100', 'White', (75, 665))
        self.drawer.drawer_text(24, f'{self.memories_value} / 5', 'White', (575, 60))

        # inventory
        pygame.draw.circle(self.display, (131, 131, 89), (WINDOW_WIDTH-60, 60), 40)
        self.inventory = pygame.image.load('map/inventory.png')
        self.display.blit(self.inventory, (WINDOW_WIDTH-92, 25))

        if self.button.inventory_button().collidepoint(pygame.mouse.get_pos()):
            self.button.inventory_button_draw_hover()
        else:
            self.button.inventory_button_draw()

        self.drawer.drawer_text(
            15, f'{self.cnt_bullet} / {self.cnt_bullet_max}', 'White', (WINDOW_WIDTH - 230, WINDOW_HEIGHT - 115))

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.button_inventory(event)

    def button_inventory(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.inventory_button().collidepoint(event.pos):
                ChangeScreen('inventory')

    def draw_minimap(self):
        coords = self.game.level.player.get_coords()
        x = coords[0]
        y = coords[1]
        self.display.blit(self.minimap, (2, 2))
        pygame.draw.circle(self.display, (255, 0, 0), (x // 20, y // 20), 5)
        pygame.draw.rect(self.display, (255, 255, 255), (0, 0, 260, 260), 2)

    def draw_weapon(self):
        weapon_images = self.weapon.images
        weapon_index = self.game.level.player.weapon_index
        pygame.draw.rect(self.display, (131, 131, 89), (WINDOW_WIDTH - 250, WINDOW_HEIGHT - 120, 256, 128))
        self.display.blit(weapon_images[weapon_index], (WINDOW_WIDTH - 250, WINDOW_HEIGHT - 115))

