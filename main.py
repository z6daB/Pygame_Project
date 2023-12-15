import pygame
from settings import *
from button import Button
from game_screens import get_current_screen, ChangeScreen

pygame.init()
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
import select_window
import choose_character


class Main:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        ChangeScreen('menu')

    def run(self):
        while True:
            get_current_screen().run()
            self.clock.tick(60)
            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    main.run()
