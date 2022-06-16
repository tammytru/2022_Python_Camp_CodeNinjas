import pygame
from pygame import *
pygame.init()

# ------- COLORS ------- #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# -- WINDOW SETTINGS -- #
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('CodeNinjas Pong')

# --- FPS SETTINGS --- #
FPS = 30 
clock = pygame.time.Clock()

# ---- PADDLE CLASS ---- #
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__() #call parent class

        self.image = pygame.Surface([width, height]) #get size
        self.image.fill(BLACK) #set background color to black
        self.image.set_colorkey(BLACK) #set it too transparent
        
        #draw the paddle. it is just a rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        #get the rectangle object using the pygame function
        self.rect = self.image.get_rect()

# ---- PADDLE OBJECT ---- #
# creating the default paddle object
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1. rect. y = 200

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 970
paddle2. rect. y = 200

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1)
all_sprites.add(paddle2)

# ----- GAME LOOP ----- #
game_running = True
while game_running:
    clock.tick(FPS)

    # =========== Process Input (EVENTS) =========== #
    for event in pygame.event.get(): #all events goes in here
        if event.type == QUIT: #if they press the 'X' button
            game_running = False

    # =================== UPDATE =================== #
    display.update() #update the display with new information
    all_sprites.update() #update all the objects in the list

    # =============== Render (DRAW) ================ #
    GAME_WINDOW.fill(BLACK) #background color
    pygame.draw.line(GAME_WINDOW, WHITE, [WINDOW_WIDTH/2, 0], [WINDOW_WIDTH/2, WINDOW_HEIGHT], 5)
    all_sprites.draw(GAME_WINDOW)

    pygame.display.flip() #must be kept at the end. after we draw everyting, flip the display
pygame.quit()


