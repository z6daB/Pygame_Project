import pygame
import sys
from button import *
from main import *

class Select:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('graphics/menu/bg.jpg')
        self.display.blit(self.bg, (0, 0))
        self.button = Button()
        self.button.button_quit_draw()
        self.button.button_settings_draw()
        self.button.button_play_draw()

    def run(self):
        self.event_loop()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()
            self.check_buttons(event)

    def check_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.button_quit().collidepoint(event.pos):
                pygame.QUIT
                sys.exit()
            if self.button.button_settings().collidepoint(event.pos):
                self.button.button_settings()
                print('settings was open')
            if self.button.button_play().collidepoint(event.pos):
                self.draw_characters()



    def draw_characters(self):
        black_man = pygame.image.load('graphics/menu/characters/character_malePerson_behindBack.png')
        woman = pygame.image.load('graphics/menu/characters/woman.png')
        white_man = pygame.image.load('graphics/menu/characters/white_man.png')
        self.display.blit(self.bg, (0, 0))
        self.display.blit(black_man, (150, 150))
        self.display.blit(woman, (550, 150))
        self.display.blit(white_man, (950, 150))
