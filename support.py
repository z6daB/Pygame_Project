import pygame
from settings import *
character = None
stats_human = black_man


def set_character(name):
    global character
    character = name


def get_character():
    return character


def set_stats(name):
    global stats_human
    stats_human = name


def get_stats():
    return stats_human

