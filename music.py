import pygame
from settings import *
pygame.mixer.music.load('sounds/music_menu.mp3')
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.3)
status = True


def change_status():
    global status
    status = not status
    play_music(status)


def get_status():
    return status


def play_music(st):
    if st is True:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
