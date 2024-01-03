import sys
import pygame
from screen import GameScreen
from game_screens import dict_screens, ChangeScreen
from button import *
from support import *
<<<<<<< HEAD
=======
from settings import *
>>>>>>> Stepan


class ChooseCharacter(GameScreen):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('graphics/menu/bg.jpg')
        self.button = Button()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check_character(event)

    def check_character(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
<<<<<<< HEAD
=======
            if self.button.button_back2().collidepoint(event.pos):
                ChangeScreen('menu')
>>>>>>> Stepan
            if self.button.black_man().collidepoint(event.pos):
                set_character('black_man')
                ChangeScreen('game')
            elif self.button.white_man().collidepoint(event.pos):

                ChangeScreen('game')

    def draw(self):
        self.button.black_man_draw()
        self.button.white_man_draw()
        black_man = pygame.image.load('graphics/menu/characters/character_malePerson_behindBack.png')
        woman = pygame.image.load('graphics/menu/characters/woman.png')
        white_man = pygame.image.load('graphics/menu/characters/white_man.png')
        self.display.blit(self.bg, (0, 0))
        self.display.blit(black_man, (150, 150))
        self.display.blit(woman, (550, 150))
        self.display.blit(white_man, (950, 150))
<<<<<<< HEAD
=======
        
        self.font = pygame.font.Font('graphics/menu/font.ttf', 30)
        self.surf_back = self.font.render('Выбор Персонажа', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), (WINDOW_WIDTH // 2 - 250, 80, 465, 50))
        self.display.blit(self.surf_back, (WINDOW_WIDTH // 2 - 240, 90))
        
        if self.button.button_back2().collidepoint(pygame.mouse.get_pos()):
            self.button.button_back_draw_hover2()
        else:
            self.button.button_back_draw2()
>>>>>>> Stepan


dict_screens['choose_char'] = ChooseCharacter()
