import pygame


def change_cursor_to_aim():
    aim_surf = pygame.image.load('../Pygame_Project-test/graphics/cursors/aim_cursor.png').convert_alpha()
    aim_cursor = pygame.cursors.Cursor((0, 0), aim_surf)
    pygame.mouse.set_cursor(aim_cursor)


def change_cursor():
    surf = pygame.image.load('../Pygame_Project-test/graphics/cursors/cursor.png').convert_alpha()
    cursor = pygame.cursors.Cursor((0, 0), surf)
    pygame.mouse.set_cursor(cursor)
