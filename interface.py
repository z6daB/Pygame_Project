import time
import pygame
from settings import *
from support import get_character, set_stats, get_stats
from game_screens import dict_screens, ChangeScreen
from drawer import Drawer


class Interface:
    def __init__(self, game):
        self.game = game

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
            self.display, (255, 0, 0), (20, 600, HEALTH_WIDTH * self.game.level.player.hp_value, HEALTH_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (0, 0, 255), (20, 630, WATER_WIDTH * self.game.level.player.water_value, WATER_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (42, 255, 4), (20, 660, RADIATION_WIDTH * self.game.level.player.radiation_value, RADIATION_HEIGHT)
        )
        pygame.draw.rect(
            self.display, (255, 222, 0), (400, 45, 100 * self.memories_value, 55)
        )
        # count
        self.drawer.drawer_text(12, f'{self.game.level.player.hp_value} / 100', 'White', (75, 605))
        self.drawer.drawer_text(12, f'{self.game.level.player.water_value} / 100', 'White', (75, 635))
        self.drawer.drawer_text(12, f'{self.game.level.player.radiation_value} / 100', 'White', (75, 665))
        self.drawer.drawer_text(24, f'{self.memories_value} / 5', 'White', (575, 60))

        # inventory
        pygame.draw.circle(self.display, (131, 131, 89), (WINDOW_WIDTH-60, 60), 40)
        self.inventory = pygame.image.load('map/inventory.png')
        self.display.blit(self.inventory, (WINDOW_WIDTH-92, 25))

        # weapon
        pygame.draw.rect(self.display, (131, 131, 89), (WINDOW_WIDTH - 250, WINDOW_HEIGHT - 120, 256, 128))
        self.weapon = pygame.image.load('graphics/weapons/stick.png')
        self.display.blit(self.weapon, (WINDOW_WIDTH - 250, WINDOW_HEIGHT - 115))
        self.drawer.drawer_text(
            15, f'{self.cnt_bullet} / {self.cnt_bullet_max}', 'White', (WINDOW_WIDTH - 230, WINDOW_HEIGHT - 115))

    def draw_minimap(self):
        coords = self.game.level.player.get_coords()
        print(coords)
        x = coords[0]
        y = coords[1]
        self.display.blit(self.minimap, (2, 2))
        pygame.draw.circle(self.display, (255, 0, 0), (x // 20, y // 20), 5)
        pygame.draw.rect(self.display, (255, 255, 255), (0, 0, 260, 260), 2)

    def update_stats(self):
        current_ticks = pygame.time.get_ticks()
        if self.game.level.player.hp_value <= 0:
            ChangeScreen('dead')
        else:
            if current_ticks - self.start_ticks > self.tick_interval:
                # проверка уровня воды
                if self.game.level.player.water_value > 0:
                    self.game.level.player.water_value -= 1
                elif self.game.level.player.water_value <= 0:
                    self.game.level.player.get_damage(1)

                # проверка уровня радиации
                if self.game.level.player.radiation_value < 100:
                    self.game.level.player.radiation_value += 5
                elif self.game.level.player.radiation_value == 100:
                    self.game.level.player.get_damage(1)

                self.start_ticks = current_ticks

    def update(self):
        self.update_stats()
