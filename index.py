import pygame, os, sys
from pytmx.util_pygame import load_pygame
from time import sleep

# ----------------------------
# SETUP
# ----------------------------

pygame.init()

def get_game_folder():
    return getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

def resource_path(relative_path):
    return os.path.join(get_game_folder(), relative_path)

game_folder = get_game_folder()

BASE_WIDTH, BASE_HEIGHT = 320, 320
win = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)

clock = pygame.time.Clock()

BLACK   = [(10, 10, 10), (50, 50, 50), (100, 100, 100), (150, 150, 150), (200, 200, 200), (250, 250, 250)]
RED     = [(100, 30, 30), (150, 50, 50), (200, 50, 50), (250, 75, 75)]
GREEN   = [(30, 100, 30), (30, 150, 30), (30, 200, 30), (50, 250, 50)]
BLUE    = [(30, 30, 100), (30, 30, 150), (30, 30, 200), (30, 30, 250)]

while True:
    win.fill(BLACK[3])
    pygame.display.flip()