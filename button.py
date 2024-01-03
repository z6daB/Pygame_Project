import pygame
from settings import *


class Button:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.font = pygame.font.Font('graphics/menu/font.ttf', 30)

    def button_quit(self):
        button_quit = pygame.Rect(WINDOW_WIDTH / 2 - 110, WINDOW_HEIGHT / 2 + 100, 135, 50)
        return button_quit

    def button_quit_draw(self):
        self.surf_quit = self.font.render('Quit', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_quit())
        self.display.blit(self.surf_quit, (self.button_quit().x + 10, self.button_quit().y + 10))

    def button_quit_draw_hover(self):
        self.surf_quit = self.font.render('Quit', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.button_quit())
        self.display.blit(self.surf_quit, (self.button_quit().x + 10, self.button_quit().y + 10))

    def button_settings(self):
        button_settings = pygame.Rect(WINDOW_WIDTH / 2 - 165, WINDOW_HEIGHT / 2, 250, 50)
        return button_settings

    def button_settings_draw(self):
        self.surf_settings = self.font.render('Settings', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_settings())
        self.display.blit(self.surf_settings, (self.button_settings().x + 10, self.button_settings().y + 10))
        
    def button_settings_draw_hover(self):
        self.surf_settings = self.font.render('Settings', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.button_settings())
        self.display.blit(self.surf_settings, (self.button_settings().x + 10, self.button_settings().y + 10))

    def button_play(self):
        button_play = pygame.Rect(WINDOW_WIDTH / 2 - 110, WINDOW_HEIGHT / 2 - 100, 150, 50)
        return button_play

    def button_play_draw(self):
        self.surf_play = self.font.render('Play', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_play())
        self.display.blit(self.surf_play, (self.button_play().x + 10, self.button_play().y + 10))
        
    def button_play_draw_hover(self):
        self.surf_play = self.font.render('Play', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.button_play())
        self.display.blit(self.surf_play, (self.button_play().x + 10, self.button_play().y + 10))

    def button_back(self):
        button_back = pygame.Rect(WINDOW_WIDTH / 2 - 110, WINDOW_HEIGHT / 2 + 100, 135, 50)
        return button_back

    def button_back_draw(self):
        self.surf_back = self.font.render('Back', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_back())
        self.display.blit(self.surf_back, (self.button_back().x + 10, self.button_back().y + 10))
      
    def button_back_draw_hover(self):
        self.surf_back = self.font.render('Back', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.button_back())
        self.display.blit(self.surf_back, (self.button_back().x + 10, self.button_back().y + 10))

    def button_check_mark(self):
        check_mark_button = pygame.Rect(WINDOW_WIDTH / 2 + 25, WINDOW_HEIGHT / 2 - 35, 40, 40)
        return check_mark_button

    def button_check_mark_draw(self):
        self.surf_check = self.font.render('Music', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_check_mark())
        self.display.blit(self.surf_check, (WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 - 25))

    def black_man(self):
        black_man_button = pygame.Rect(150, 150, 192, 256)
        return black_man_button

    def black_man_draw(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.black_man())

    def white_man(self):
        white_man_button = pygame.Rect(950, 150, 192, 256)
        return white_man_button

    def white_man_draw(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.white_man())

    def woman(self):
        pass

    def woman_draw(self):
        pass
        
    def button_back2(self):
        button_back = pygame.Rect(0, WINDOW_HEIGHT-50, 135, 50)
        return button_back

    def button_back_draw2(self):
        self.surf_back = self.font.render('Back', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_back2())
        self.display.blit(self.surf_back, (self.button_back2().x + 10, self.button_back2().y + 10))
      
    def button_back_draw_hover2(self):
        self.surf_back = self.font.render('Back', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.button_back2())
        self.display.blit(self.surf_back, (self.button_back2().x + 10, self.button_back2().y + 10))

    def menu_button(self):
        menu_button = pygame.Rect(WINDOW_WIDTH // 2 - 140, WINDOW_HEIGHT // 2 - 50, 150, 50)
        return menu_button

    def menu_button_draw(self):
        self.surf_menu = self.font.render('Menu', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.menu_button())
        self.display.blit(self.surf_menu, (self.menu_button().x + 15, self.menu_button().y + 10))

    def restart_button(self):
        restart_button = pygame.Rect(WINDOW_WIDTH // 2 - 175, WINDOW_HEIGHT // 2 + 50, 230, 50)
        return restart_button

    def restart_button_draw(self):
        self.surf_restart = self.font.render('Restart', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.restart_button())
        self.display.blit(self.surf_restart, (self.restart_button().x + 15, self.restart_button().y + 10))

    def dead_inscription(self):
        self.surf_dead = self.font.render('You lost', True, 'Black')
        self.display.blit(self.surf_dead, (WINDOW_WIDTH // 2 - 180, 200))

