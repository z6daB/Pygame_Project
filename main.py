import pygame
from settings import *
from game_screens import get_current_screen, ChangeScreen, add_screen
from change_cursor import change_cursor

pygame.init()
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
import select_window
from choose_character import ChooseCharacter
import loading
import inventory
import crafter
import settings_window
import level
from game import Game
import loss_screen
import final_window


class Main:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.game = Game()
        add_screen('game', self.game)
        add_screen('choose_char', ChooseCharacter(self.game))
        pygame.display.set_caption('Battle Among the Ruins')
        change_cursor()
        ChangeScreen('menu')

    def run(self):
        while True:
            get_current_screen().run()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    main = Main()
    main.run()
