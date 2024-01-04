import pygame
import sys
from screen import GameScreen
from game_screens import dict_screens, ChangeScreen
from button import *


class DeadWindow(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('../Pygame_Project-test/graphics/menu/bg.jpg')
        self.button = Button()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check_buttons(event)

    def check_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.menu_button().collidepoint(event.pos):
                ChangeScreen('menu')
            elif self.button.restart_button().collidepoint(event.pos):
                ChangeScreen('load')

    def draw(self):
        self.display.blit(self.bg, (0, 0))
        self.button.menu_button_draw()
        self.button.restart_button_draw()
        self.button.dead_inscription()


dict_screens['dead'] = DeadWindow()
