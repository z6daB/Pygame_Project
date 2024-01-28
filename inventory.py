import sys
import pygame
from screen import GameScreen
from game_screens import dict_screens, ChangeScreen
from button import *
from support import *
from settings import *
from drawer import *
from button import Button
from drawer import *


class Inventory(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.button = Button()
        self.drawer = Drawer()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check(event)

    def check(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.inventory_back_button().collidepoint(event.pos):
                ChangeScreen('game')
            elif self.button.button_slot_crafter().collidepoint(event.pos):
                ChangeScreen('crafter')

    def draw(self):
        pygame.draw.rect(self.display, (102, 102, 51), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.draw.rect(self.display, (155, 155, 115), (75, 80, WINDOW_WIDTH - 200, WINDOW_HEIGHT - 100))
        # inventory
        self.button.button_slot_inventory_draw_hover()
        # crafter
        if self.button.button_slot_crafter().collidepoint(pygame.mouse.get_pos()):
            self.button.button_slot_crafter_draw_hover()
        else:
            self.button.button_slot_crafter_draw()
        # back
        if self.button.inventory_back_button().collidepoint(pygame.mouse.get_pos()):
            self.button.inventory_back_button_draw_hover()
        else:
            self.button.inventory_back_button_draw()
        self.drawer.inventory_draw()


dict_screens['inventory'] = Inventory()
