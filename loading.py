import pygame
import sys
from button import *
from game_screens import dict_screens, ChangeScreen
from screen import GameScreen


class Load(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('../Pygame_Project-test/graphics/menu/bg.jpg')
        self.cnt = 0

    def draw(self):
        self.display.blit(self.bg, (0, 0))
        pygame.draw.rect(self.display, (102, 102, 51), (WINDOW_WIDTH // 2 - 250, 250, 465, 50))
        self.font = pygame.font.Font('../Pygame_Project-test/graphics/menu/font.ttf', 30)
        self.surf_back = self.font.render('   Loading...', True, 'Black')
        self.display.blit(self.surf_back, (WINDOW_WIDTH // 2 - 240, 260))
        
        pygame.draw.rect(self.display, (255, 255, 255), (WINDOW_WIDTH // 2 - 325, 315, 600, 50), 10, 20)
        if self.cnt != 595:
            pygame.draw.rect(self.display, (255, 255, 255), (WINDOW_WIDTH // 2 - 320, 325, self.cnt, 30), 0, 20)
            self.cnt += 5
        else:
            ChangeScreen('game')
            self.cnt = 0

dict_screens['load'] = Load()