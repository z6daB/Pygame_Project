import pygame
character = None


def set_character(name):
    global character
    character = name


def get_character():
    return character
