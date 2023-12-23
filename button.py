import pygame
from settings import *


class Button:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font('graphics/menu/font.ttf', 30)

    def button_quit(self):
        button_quit = pygame.Rect(WINDOW_WIDTH / 2 - 110, WINDOW_HEIGHT / 2 + 100, 135, 50)
        return button_quit

    def button_quit_draw(self):
        self.surf_quit = self.font.render('Quit', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_quit())
        self.display.blit(self.surf_quit, (self.button_quit().x + 10, self.button_quit().y + 10))

    def button_settings(self):
        button_settings = pygame.Rect(WINDOW_WIDTH / 2 - 165, WINDOW_HEIGHT / 2, 250, 50)
        return button_settings

    def button_settings_draw(self):
        self.surf_settings = self.font.render('Settings', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_settings())
        self.display.blit(self.surf_settings, (self.button_settings().x + 10, self.button_settings().y + 10))
# test
    def button_play(self):
        button_play = pygame.Rect(WINDOW_WIDTH / 2 - 110, WINDOW_HEIGHT / 2 - 100, 150, 50)
        return button_play

    def button_play_draw(self):
        self.surf_play = self.font.render('Play', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_play())
        self.display.blit(self.surf_play, (self.button_play().x + 10, self.button_play().y + 10))

    def button_back(self):
        button_back = pygame.Rect(WINDOW_WIDTH / 2 - 110, WINDOW_HEIGHT / 2 + 100, 135, 50)
        return button_back

    def button_back_draw(self):
        self.surf_back = self.font.render('Back', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_back())
        self.display.blit(self.surf_back, (self.button_back().x + 10, self.button_back().y + 10))

    def button_check_mark(self):
        check_mark_button = pygame.Rect(WINDOW_WIDTH / 2 + 25, WINDOW_HEIGHT / 2 - 35, 40, 40)
        return check_mark_button

    def button_check_mark_draw(self):
        self.surf_check = self.font.render('Music', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_check_mark())
        self.display.blit(self.surf_check, (WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 - 25))

    def black_man(self):
        black_man_button = pygame.Rect(150, 150, 192, 256)
        return black_man_button

    def draw_black_man(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.black_man())
