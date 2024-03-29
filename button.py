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

    def button_black_man(self):
        button_back = pygame.Rect(125, 170, 250, 350)
        return button_back

    def button_black_man_draw(self):
        pygame.draw.rect(self.display, (102, 102, 51), self.button_black_man())

    def button_black_man_draw_hover(self):
        pygame.draw.rect(self.display, (131, 131, 89), self.button_black_man())

    def button_woman(self):
        button_back = pygame.Rect(525, 170, 250, 350)
        return button_back

    def button_woman_draw(self):
        pygame.draw.rect(self.display, (102, 102, 51), self.button_woman())

    def button_woman_draw_hover(self):
        pygame.draw.rect(self.display, (131, 131, 89), self.button_woman())

    def button_white_man(self):
        button_back = pygame.Rect(925, 170, 250, 350)
        return button_back

    def button_white_man_draw(self):
        pygame.draw.rect(self.display, (102, 102, 51), self.button_white_man())

    def button_white_man_draw_hover(self):
        pygame.draw.rect(self.display, (131, 131, 89), self.button_white_man())
        
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
        
    def menu_button_draw_hover(self):
        self.surf_menu = self.font.render('Menu', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.menu_button())
        self.display.blit(self.surf_menu, (self.menu_button().x + 15, self.menu_button().y + 10))

    def restart_button(self):
        restart_button = pygame.Rect(WINDOW_WIDTH // 2 - 175, WINDOW_HEIGHT // 2 + 50, 230, 50)
        return restart_button

    def restart_button_draw(self):
        self.surf_restart = self.font.render('Restart', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.restart_button())
        self.display.blit(self.surf_restart, (self.restart_button().x + 15, self.restart_button().y + 10))
    
    def restart_button_draw_hover(self):
        self.surf_restart = self.font.render('Restart', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.restart_button())
        self.display.blit(self.surf_restart, (self.restart_button().x + 15, self.restart_button().y + 10))

    def dead_inscription(self):
        self.surf_dead = self.font.render('You lost', True, 'Black')
        self.display.blit(self.surf_dead, (WINDOW_WIDTH // 2 - 180, 200))
        
    def inventory_button(self):
        inventory_button = pygame.Rect(WINDOW_WIDTH - 110, 10, 80, 80)
        return inventory_button

    def inventory_button_draw(self):
        pygame.draw.circle(self.display, (102, 102, 51), (WINDOW_WIDTH-60, 60), 40)
        self.inventory = pygame.image.load('map/inventory.png')
        self.display.blit(self.inventory, (WINDOW_WIDTH-92, 25))
    
    def inventory_button_draw_hover(self):
        pygame.draw.circle(self.display, (131, 131, 89), (WINDOW_WIDTH-60, 60), 40)
        self.inventory = pygame.image.load('map/inventory.png')
        self.display.blit(self.inventory, (WINDOW_WIDTH-92, 25))
        
    def inventory_back_button(self):
        inventory_button = pygame.Rect(WINDOW_WIDTH - 110, 10, 80, 80)
        return inventory_button

    def inventory_back_button_draw(self):
        pygame.draw.circle(self.display, (131, 131, 89), (WINDOW_WIDTH-60, 60), 40)
        self.inventory = pygame.image.load('map/inventory_back.png')
        self.display.blit(self.inventory, (WINDOW_WIDTH-92, 30))
    
    def inventory_back_button_draw_hover(self):
        pygame.draw.circle(self.display, (155, 155, 115), (WINDOW_WIDTH-60, 60), 40)
        self.inventory = pygame.image.load('map/inventory_back.png')
        self.display.blit(self.inventory, (WINDOW_WIDTH-92, 30))
        
    def button_slot_inventory(self):
        button_back = pygame.Rect(200, 20, 300, 60)
        return button_back

    def button_slot_inventory_draw(self):
        self.surf_back = self.font.render('Inventory', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.button_slot_inventory())
        self.display.blit(self.surf_back, (self.button_slot_inventory().x + 15, self.button_slot_inventory().y + 15))

    def button_slot_inventory_draw_hover(self):
        self.surf_back = self.font.render('Inventory', True, 'Black')
        pygame.draw.rect(self.display, (155, 155, 115), self.button_slot_inventory())
        self.display.blit(self.surf_back, (self.button_slot_inventory().x + 15, self.button_slot_inventory().y + 15))        

    def button_slot_crafter(self):
        button_back = pygame.Rect(700, 20, 240, 60)
        return button_back

    def button_slot_crafter_draw(self):
        self.surf_back = self.font.render('Crafter', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.button_slot_crafter())
        self.display.blit(self.surf_back, (self.button_slot_crafter().x + 15, self.button_slot_crafter().y + 15))

    def button_slot_crafter_draw_hover(self):
        self.surf_back = self.font.render('Crafter', True, 'Black')
        pygame.draw.rect(self.display, (155, 155, 115), self.button_slot_crafter())
        self.display.blit(self.surf_back, (self.button_slot_crafter().x + 15, self.button_slot_crafter().y + 15))
    # slot1
    def button_craft_slot1(self):
        button_back = pygame.Rect(150 - 7, 180 - 7, 150+14, 150+14)
        return button_back

    def button_craft_slot1_draw(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.button_craft_slot1(), 7, 3)
        
    def button_craft_slot1_draw_hover(self):
        pygame.draw.rect(self.display, (255, 0, 0), self.button_craft_slot1(), 7, 3)
    # slot2
    def button_craft_slot2(self):
        button_back = pygame.Rect(150 + 200 -7, 180-7, 150+14, 150+14)
        return button_back

    def button_craft_slot2_draw(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.button_craft_slot2(), 7, 3)
        
    def button_craft_slot2_draw_hover(self):
        pygame.draw.rect(self.display, (255, 0, 0), self.button_craft_slot2(), 7, 3)
    # slot3
    def button_craft_slot3(self):
        button_back = pygame.Rect(150 + 200 * 2-7, 180 -7, 150+14, 150+14)
        return button_back

    def button_craft_slot3_draw(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.button_craft_slot3(), 7, 3)
        
    def button_craft_slot3_draw_hover(self):
        pygame.draw.rect(self.display, (255, 0, 0), self.button_craft_slot3(), 7, 3)
    # slot4
    def button_craft_slot4(self):
        button_back = pygame.Rect(150 -7, 180 + 230 -7, 150+14, 150+14)
        return button_back

    def button_craft_slot4_draw(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.button_craft_slot4(), 7, 3)
        
    def button_craft_slot4_draw_hover(self):
        pygame.draw.rect(self.display, (255, 0, 0), self.button_craft_slot4(), 7, 3)
    # slot5
    def button_craft_slot5(self):
        button_back = pygame.Rect(150 + 200 -7, 180 + 230 -7, 150+14, 150+14)
        return button_back

    def button_craft_slot5_draw(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.button_craft_slot5(), 7, 3)
        
    def button_craft_slot5_draw_hover(self):
        pygame.draw.rect(self.display, (255, 0, 0), self.button_craft_slot5(), 7, 3)
    # slot6
    def button_craft_slot6(self):
        button_back = pygame.Rect(150 + 200 * 2-7, 180 + 230 -7, 150+14, 150+14)
        return button_back

    def button_craft_slot6_draw(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.button_craft_slot6(), 7, 3)
        
    def button_craft_slot6_draw_hover(self):
        pygame.draw.rect(self.display, (255, 0, 0), self.button_craft_slot6(), 7, 3)
    
    def button_craft(self):
        button_play = pygame.Rect(WINDOW_WIDTH - 450, WINDOW_HEIGHT - 125, 225, 70)
        return button_play

    def button_craft_draw(self):
        self.surf_play = self.font.render('Crafter', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_craft())
        self.display.blit(self.surf_play, (self.button_craft().x + 10, self.button_craft().y + 20))

    def button_craft_draw_hover(self):
        self.surf_play = self.font.render('Crafter', True, 'Black')
        pygame.draw.rect(self.display, (131, 131, 89), self.button_craft())
        self.display.blit(self.surf_play, (self.button_craft().x + 10, self.button_craft().y + 20))

    def button_win(self):
        button_win = pygame.Rect(WINDOW_WIDTH / 2 - 165, WINDOW_HEIGHT / 2 - 150, 210, 50)
        return button_win

    def button_win_draw(self):
        self.surf_win = self.font.render('You won', True, 'Black')
        pygame.draw.rect(self.display, (102, 102, 51), self.button_win())
        self.display.blit(self.surf_win, (self.button_win().x, self.button_win().y + 10))