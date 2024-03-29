import sys
import pygame
from screen import GameScreen
from game_screens import dict_screens, ChangeScreen
from button import *
from settings import *
from drawer import *
from player import Player
from support import set_character
from game import Game


class ChooseCharacter(GameScreen):
    def __init__(self, game):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load('graphics/menu/bg.jpg')
        self.button = Button()
        self.drawer = Drawer()
        self.game = game

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.check_character(event)

    def check_character(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.button_back2().collidepoint(event.pos):
                ChangeScreen('menu')
            if self.button.button_black_man().collidepoint(event.pos):
                self.game = Game()
                dict_screens['game'] = self.game
                set_character('black_man')
                dict_screens['game'].level.spawn_player(
                    Player(dict_screens['game'].level.visible_sprites,
                           dict_screens['game'].level.invisible_sprites, self.game, 0, 1, 1, **black_man))
                ChangeScreen('load')
            elif self.button.button_woman().collidepoint(event.pos):
                self.game = Game()
                dict_screens['game'] = self.game
                set_character('woman')
                dict_screens['game'].level.spawn_player(
                    Player(dict_screens['game'].level.visible_sprites,
                           dict_screens['game'].level.invisible_sprites, self.game, 0, 0, 1, **woman))
                ChangeScreen('load')
            elif self.button.button_white_man().collidepoint(event.pos):
                self.game = Game()
                dict_screens['game'] = self.game
                set_character('white_man')
                dict_screens['game'].level.spawn_player(
                    Player(dict_screens['game'].level.visible_sprites,
                           dict_screens['game'].level.invisible_sprites, self.game, 0, 1, 1, **white_man))
                ChangeScreen('load')

    def draw(self):
        black_man = pygame.image.load(
            'graphics/menu/characters/character_malePerson_behindBack.png')
        woman = pygame.image.load('graphics/menu/characters/woman.png')
        white_man = pygame.image.load('graphics/menu/characters/white_man.png')
        self.display.blit(self.bg, (0, 0))
        # black_man
        if self.button.button_black_man().collidepoint(pygame.mouse.get_pos()):
            self.button.button_black_man_draw_hover()
        else:
            self.button.button_black_man_draw()
        self.drawer.black_man_stat_draw()
        # woman
        if self.button.button_woman().collidepoint(pygame.mouse.get_pos()):
            self.button.button_woman_draw_hover()
        else:
            self.button.button_woman_draw()
        self.drawer.woman_stat_draw()
        # white_man
        if self.button.button_white_man().collidepoint(pygame.mouse.get_pos()):
            self.button.button_white_man_draw_hover()
        else:
            self.button.button_white_man_draw()
        self.drawer.white_man_stat_draw()

        self.display.blit(black_man, (150, 145))
        self.display.blit(woman, (550, 145))
        self.display.blit(white_man, (950, 145))

        self.drawer.title_draw()
        if self.button.button_back2().collidepoint(pygame.mouse.get_pos()):
            self.button.button_back_draw_hover2()
        else:
            self.button.button_back_draw2()
