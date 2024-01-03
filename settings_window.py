import pygame
import sys
from button import *
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen
from music import *


class Settings(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('graphics/menu/bg.jpg')
        self.check_mark = pygame.image.load('graphics/menu/check_mark.png')
        self.button = Button()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check_buttons(event)

    def check_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.button_back().collidepoint(event.pos):
                ChangeScreen('menu')
            if self.button.button_check_mark().collidepoint(event.pos):
                change_status()

    def draw(self):
        self.display.blit(self.bg, (0, 0))
        self.button.button_check_mark_draw()
        if self.button.button_back().collidepoint(pygame.mouse.get_pos()):
            self.button.button_back_draw_hover()
        else:
            self.button.button_back_draw()
        if get_status():
            self.display.blit(self.check_mark, (WINDOW_WIDTH / 2 + 30, WINDOW_HEIGHT / 2 - 30))


dict_screens['settings_window'] = Settings()
