import pygame
from settings import *
from game_screens import get_current_screen, ChangeScreen
from change_cursor import change_cursor
pygame.init()
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
import select_window
import choose_character
import settings_window
import level
import game


class Main:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        change_cursor()
        pygame.display.set_caption('Battle Among the Ruins')
        ChangeScreen('menu')

    def run(self):
        while True:
            get_current_screen().run()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    main = Main()
    main.run()
