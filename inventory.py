import sys
import pygame
from screen import GameScreen
from game_screens import dict_screens, ChangeScreen
from button import *
from support import *
from settings import *
from drawer import *
from button import Button


class Inventory(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.button = Button()

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

    def draw(self):
        pygame.draw.rect(self.display, (255, 255, 255), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        # back
        if self.button.inventory_back_button().collidepoint(pygame.mouse.get_pos()):
            self.button.inventory_back_button_draw_hover()
        else:
            self.button.inventory_back_button_draw()



dict_screens['inventory'] = Inventory()
