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
from item import Item
from game import Game


class Crafter(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.button = Button()
        self.drawer = Drawer()
        self.item = Item()
        self.active_now = 1

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check(event)
            self.update()

    def check(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.inventory_back_button().collidepoint(event.pos):
                ChangeScreen('game')
            elif self.button.button_slot_inventory().collidepoint(event.pos):
                ChangeScreen('inventory')
            elif self.button.button_craft_slot1().collidepoint(event.pos):
                self.active_now = 1
            elif self.button.button_craft_slot2().collidepoint(event.pos):
                self.active_now = 2
            elif self.button.button_craft_slot3().collidepoint(event.pos):
                self.active_now = 3
            elif self.button.button_craft_slot4().collidepoint(event.pos):
                self.active_now = 4
            elif self.button.button_craft_slot5().collidepoint(event.pos):
                self.active_now = 5
            elif self.button.button_craft_slot6().collidepoint(event.pos):
                self.active_now = 6
            elif self.button.button_craft().collidepoint(event.pos):
                if self.active_now  == 1:
                    pass
                elif self.active_now  == 2:
                    pass
                elif self.active_now  == 3:
                    pass
                elif self.active_now  == 4:
                    pass
                elif self.active_now  == 5:
                    pass
                elif self.active_now  == 6:
                    pass

    def draw(self):
        pygame.draw.rect(self.display, (102, 102, 51), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.draw.rect(self.display, (155, 155, 115), (75, 80, WINDOW_WIDTH - 200, WINDOW_HEIGHT - 100))
        # inventory
        if self.button.button_slot_inventory().collidepoint(pygame.mouse.get_pos()):
            self.button.button_slot_inventory_draw_hover()
        else:
            self.button.button_slot_inventory_draw()
        # crafter
        self.button.button_slot_crafter_draw_hover()
        # back
        if self.button.inventory_back_button().collidepoint(pygame.mouse.get_pos()):
            self.button.inventory_back_button_draw_hover()
        else:
            self.button.inventory_back_button_draw()
        self.drawer.crafter_draw()
        # slot1
        if self.active_now == 1:
            self.button.button_craft_slot1_draw_hover()
        else:
            self.button.button_craft_slot1_draw()
        # slot2
        if self.active_now == 2:
            self.button.button_craft_slot2_draw_hover()
        else:
            self.button.button_craft_slot2_draw()
        # slot3
        if self.active_now == 3:
            self.button.button_craft_slot3_draw_hover()
        else:
            self.button.button_craft_slot3_draw()
        # slot4
        if self.active_now == 4:
            self.button.button_craft_slot4_draw_hover()
        else:
            self.button.button_craft_slot4_draw()
        # slot5
        if self.active_now == 5:
            self.button.button_craft_slot5_draw_hover()
        else:
            self.button.button_craft_slot5_draw()
        # slot6
        if self.active_now == 6:
            self.button.button_craft_slot6_draw_hover()
        else:
            self.button.button_craft_slot6_draw()
        
        self.drawer.crafter_slot_draw(self.active_now - 1)
        # crafter
        if self.button.button_craft().collidepoint(pygame.mouse.get_pos()):
            self.button.button_craft_draw_hover()
        else:
            self.button.button_craft_draw()

    def update(self):
        self.weapon_have = dict_screens['game'].level.player.weapon_have
        self.item_have = dict_screens['game'].level.player.item_have


dict_screens['crafter'] = Crafter()
