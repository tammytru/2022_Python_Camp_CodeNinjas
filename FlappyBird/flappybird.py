from tkinter import SCROLL
import pygame
from pygame import *
import random
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

PIPE_GAP = 150
PIPE_FREQUENCY = 1500 #milliseconds
LAST_PIPE = pygame.time.get_ticks() - PIPE_FREQUENCY

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

# ========== PIPES =========== #
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('FlappyBird/assets/pipe.png')
        self.rect = self.image.get_rect()

        if position == 1: #at top
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(PIPE_GAP/2)]
        if position == -1: #at bottom
            self.rect.topleft = [x, y + int(PIPE_GAP/2)]

    def update(self):
        self.rect.x -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()

pipe_group = pygame.sprite.Group()

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
    
    #if bird touch pipe
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or bird.rect.top < 0:
        GAME_OVER = True
    
    #if bird hit ground
    if bird.rect.bottom >= 768:
        GAME_OVER = True
        FLYING = False

    # -------- UPDATE -------- #
    pygame.display.update()
    if GAME_OVER == False and FLYING:
        GROUND_SCROLL -= SCROLL_SPEED
        if abs(GROUND_SCROLL) > 35:
            GROUND_SCROLL = 0

        curr_time = pygame.time.get_ticks()
        if curr_time - LAST_PIPE > PIPE_FREQUENCY:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(WINDOW_WIDTH, int(WINDOW_HEIGHT/2) + pipe_height, -1)
            top_pipe = Pipe(WINDOW_WIDTH, int(WINDOW_HEIGHT/2) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            LAST_PIPE = curr_time

        pipe_group.update()
        bird_group.update()

    if bird.rect.bottom > 768:
        GAME_OVER = True
        FLYING = False
    # -------- RENDER -------- #
    GAME_WINDOW.blit(background_img, (0,0)) 
    GAME_WINDOW.blit(ground_img, (GROUND_SCROLL, 768))

    bird_group.draw(GAME_WINDOW)
    pipe_group.draw(GAME_WINDOW)

    pygame.display.flip()
pygame.quit()