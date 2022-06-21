from tkinter import SCROLL
import pygame
from pygame import *
pygame.init()

# ========== COLORS ========== #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ===== WINDOW SETTINGS ====== #
WINDOW_WIDTH = 864
WINDOW_HEIGHT = 936
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Flappy Bird')

# ====== GAME SETTINGS ======= #
FPS = 60
clock = pygame.time.Clock()

GROUND_SCROLL = 0
SCROLL_SPEED = 4
FLYING = False
GAME_OVER = False

# ========== BIRD =========== #
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('FlappyBird/assets/bird1.png')
        self.index = 0
        self.counter = 0
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.pressed = False
    
    def update(self):
        if FLYING == True:
            #gravity
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
        if GAME_OVER == False:
            #jump
            if pygame.key.get_pressed()[K_SPACE] and self.pressed == False:
                self.pressed = True
                self.vel = -10
            if not pygame.key.get_pressed()[K_SPACE]:
                self.pressed = False

bird_group = pygame.sprite.Group()
bird = Bird(100, (WINDOW_HEIGHT/2))
bird_group.add(bird)

# ======= LOAD IMAGES ========= #
background_img = pygame.image.load('FlappyBird/assets/bg.png')
ground_img = pygame.image.load('FlappyBird/assets/ground.png')

# ======== GAME LOOP ========= #
game_running = True
while game_running:
    clock.tick(FPS)

    # -------- EVENTS -------- #
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                FLYING = True
            if event.key == K_ESCAPE:
                game_running = False
    
    # -------- UPDATE -------- #
    pygame.display.update()
    if GAME_OVER == False:
        GROUND_SCROLL -= SCROLL_SPEED
        if abs(GROUND_SCROLL) > 35:
            GROUND_SCROLL = 0

    bird_group.update()
    if bird.rect.bottom > 768:
        GAME_OVER = True
        FLYING = False
    # -------- RENDER -------- #
    GAME_WINDOW.blit(background_img, (0,0)) 
    GAME_WINDOW.blit(ground_img, (GROUND_SCROLL, 768))

    bird_group.draw(GAME_WINDOW)

    pygame.display.flip()
pygame.quit()