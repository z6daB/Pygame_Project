import pygame
from settings import *
from button import Button
from select_window import *


class Main:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load('graphics/menu/bg.jpg')
        self.display.blit(self.bg, (0, 0))
        self.button = Button()
        self.select = Select()

    def run(self):
        running = True
        self.button.button_quit_draw()
        self.button.button_settings_draw()
        self.button.button_play_draw()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.button.button_quit().collidepoint(event.pos):
                        running = False
                    if self.button.button_settings().collidepoint(event.pos):
                        print('settings was open')
                    if self.button.button_play().collidepoint(event.pos):
                        print('Playing screen')
                        self.display.blit(self.bg, (0, 0))


            self.clock.tick(60)
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
    #tetst
