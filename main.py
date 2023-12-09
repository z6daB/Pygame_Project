import pygame
from settings import *


class Main:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load('graphics/menu/bg.jpg')
        self.display.blit(self.bg, (0, 0))

    def run(self):
        font = pygame.font.Font('graphics/menu/font.ttf', 30)
        surf = font.render('Quit', True, 'Black')
        button_quit = pygame.Rect(WINDOW_WIDTH / 2 - 110, WINDOW_HEIGHT / 2 + 100, 135, 50)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_quit.collidepoint(event.pos):
                        running = False
            pygame.draw.rect(self.display, (102, 102, 51), button_quit)
            self.display.blit(surf, (button_quit.x + 10, button_quit.y + 10))
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
