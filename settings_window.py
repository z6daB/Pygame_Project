import pygame
import sys
from button import *
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen


class Settings(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('graphics/menu/bg.jpg')
        self.button = Button()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()
            self.check_buttons(event)

    def check_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.button_back().collidepoint(event.pos):
                ChangeScreen('menu')

    def draw(self):
        self.display.blit(self.bg, (0, 0))
        self.button.button_back_draw()


dict_screens['settings_window'] = Settings()
