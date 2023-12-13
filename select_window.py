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
                print('settings was open')
            if self.button.button_play().collidepoint(event.pos):
                self.playing_screen()



    def playing_screen(self):
        print('Playing screen')
        self.display.blit(self.bg, (0, 0))