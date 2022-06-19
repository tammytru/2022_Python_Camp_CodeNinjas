from random import randint
import pygame
from pygame import *
pygame.init()

# ------- COLORS ------- #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# -------- TEXT -------- #
TEXTSIZE = 30
font = pygame.font.Font(None, TEXTSIZE)

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

    def moveUp(self, pixels): 
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0
    def moveDown(self, pixels): 
        self.rect.y += pixels
        if self.rect.y > WINDOW_HEIGHT - 100:
            self.rect.y = WINDOW_HEIGHT - 100

# ------- BALL CLASS ------- #
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4,8), randint(-8,8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

# ---- CREATING OBJECTS ---- #
# creating the default paddle object
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1. rect. y = 200

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 970
paddle2. rect. y = 200

# creating the ball object
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1)
all_sprites.add(paddle2)
all_sprites.add(ball)

# --- SCORING SYSTEM --- #
p1Score = 0
p2Score = 0

# ----- GAME LOOP ----- #
game_running = True
while game_running:
    clock.tick(FPS)

    # =========== Process Input (EVENTS) =========== #
    for event in pygame.event.get(): #all events goes in here
        if event.type == QUIT: #if they press the 'X' button
            game_running = False

    #moving the paddles based on keys pressed
    keys = pygame.key.get_pressed() #get the key that was pressed
    if keys[pygame.K_w]:
        paddle1.moveUp(5)
    if keys[pygame.K_s]:
        paddle1.moveDown(5)
    if keys[pygame.K_UP]:
        paddle2.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddle2.moveDown(5)

    # =================== UPDATE =================== #
    display.update() #update the display with new information
    all_sprites.update() #update all the objects in the list

    #checking if ball touches a wall
    if ball.rect.x <= 0: #left wall
        pygame.time.wait(300)
        ball.rect.x = WINDOW_WIDTH/4
        ball.rect.y = WINDOW_HEIGHT/2
        ball.velocity[0] = -ball.velocity[0]
        p2Score += 1
    if ball.rect.x >= WINDOW_WIDTH - 10: #right wall
        pygame.time.wait(300)
        ball.rect.x = (WINDOW_WIDTH/4) * 3
        ball.rect.y = WINDOW_HEIGHT/2
        ball.velocity[0] = -ball.velocity[0]
        p1Score += 1
    if ball.rect.y < 0: #top wall
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y > WINDOW_HEIGHT - 10: #bottom wall
        ball.velocity[1] = - ball.velocity[1]
    
    #collision detection - ball hit paddle
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        ball.bounce()

    #updating text
    text1 = font.render(str(p1Score), 1, WHITE)
    text2 = font.render(str(p2Score), 1, WHITE)

    # =============== Render (DRAW) ================ #
    GAME_WINDOW.fill(BLACK) #background color
    pygame.draw.line(GAME_WINDOW, WHITE, [WINDOW_WIDTH/2, 0], [WINDOW_WIDTH/2, WINDOW_HEIGHT], 5)
    all_sprites.draw(GAME_WINDOW)

    GAME_WINDOW.blit(text1, (WINDOW_WIDTH/2 - 35, 10))
    GAME_WINDOW.blit(text2, (WINDOW_WIDTH/2 + 20, 10))

    pygame.display.flip() #must be kept at the end. after we draw everyting, flip the display
pygame.quit()


