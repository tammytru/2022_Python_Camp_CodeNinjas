import pygame
from pygame import *
pygame.init()

#===== WINDOWS AND BACKGROUND =====#
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('CodeNinjas Pong')

background_img = image.load('pong_background.png')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, (WINDOW_WIDTH, WINDOW_HEIGHT))

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
    display.update()


pygame.quit()


