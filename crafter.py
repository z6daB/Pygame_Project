import sys
from random import choices, random
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
        self.status_res = 0
        self.res_yes = pygame.image.load('graphics/crafter/yes.png')
        self.res_no = pygame.image.load('graphics/crafter/no.png')

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check(event)
            self.update()

    def check(self, event):
        self.weapon_have = dict_screens['game'].level.player.weapon_have
        self.item_have = dict_screens['game'].level.player.item_have
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
                elem = self.item.formula_craft[self.item.items_crafter[self.active_now - 1]]
                flag = True
                for i in range(len(elem)):
                    for j in range(len(self.item_have)):
                        if self.item_have[j][0] == elem[i][0]:
                            if elem[i][1] > self.item_have[j][1]:
                                flag = False
                                break
                if flag:
                    self.status_res = 1
                    for i in range(len(elem)):
                        for j in range(len(self.item_have)):
                            if self.item_have[j][0] == elem[i][0]:
                                if elem[i][1] <= self.item_have[j][1]:
                                    self.item_have[j][1] -= elem[i][1]
                    if self.active_now == 1:
                        dict_screens['game'].level.player.hp_value += 10
                    elif self.active_now == 2:
                        dict_screens['game'].level.player.radiation_value -= 20
                    elif self.active_now == 3:
                        dict_screens['game'].level.player.water_value += 20
                    elif self.active_now == 4:
                        elem = dict_screens['game'].level.player.weapon_have
                        for i in range(len(elem)):
                            if elem[i][0] == 'handgun':
                                dict_screens['game'].level.player.weapon_have[i][3] = 1
                    elif self.active_now == 5:
                        elem = dict_screens['game'].level.player.weapon_have
                        for i in range(len(elem)):
                            if elem[i][0] == 'gun':
                                dict_screens['game'].level.player.weapon_have[i][3] = 1
                    elif self.active_now == 6:
                        dict_screens['game'].level.player.bullets_have += 5

                    num = random()
                    if 1 - num <= 0.04:
                        dict_screens['game'].level.player.memories_value += 1
                else:
                    self.status_res = -1

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
        # buy result
        if self.status_res == 1:
            self.display.blit(self.res_yes, (1060, 605))
        elif self.status_res == -1:
            self.display.blit(self.res_no, (1060, 605))

    def update(self):
        self.weapon_have = dict_screens['game'].level.player.weapon_have
        self.item_have = dict_screens['game'].level.player.item_have


dict_screens['crafter'] = Crafter()
