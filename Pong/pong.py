import pygame
from pygame import *
pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('CodeNinjas Pong')



game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
    display.update()


pygame.quit()


