import pygame
from settings import *
from button import Button
from select_window import *


class Main:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.select = Select()

    def run(self):
        while True:
            self.select.run()
            self.clock.tick(60)
            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    main.run()
    #tetst
