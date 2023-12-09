import pygame
from settings import *


class Button:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font('graphics/menu/font.ttf', 30)
        self.surf = self.font.render('Quit', True, 'Black')

    def button_quit(self):
        button_quit = pygame.Rect(WINDOW_WIDTH / 2 - 110, WINDOW_HEIGHT / 2 + 100, 135, 50)
        return button_quit

    def button_quit_draw(self):
        pygame.draw.rect(self.display, (102, 102, 51), self.button_quit())
        self.display.blit(self.surf, (self.button_quit().x + 10, self.button_quit().y + 10))
# test