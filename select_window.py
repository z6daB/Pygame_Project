import pygame

class Select:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.event_loop()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
            self.check_buttons(event)

    def check_buttons(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.button_quit().collidepoint(event.pos):
                pygame.QUIT
