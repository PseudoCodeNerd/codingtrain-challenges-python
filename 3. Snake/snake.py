import pygame
import random
import sys

# Settings for Window size
HORIZONTAL_PIXELS = 30
VERTICAL_PIXELS = 20

# Settings for the graphics
FPS = 10
PIXEL_SIZE = 40

# Color constants
SNAKE_COLOR = 46, 125, 50
FOOD_COLOR = 216, 67, 21
BLACK = 40, 40, 40

# Fix Window size according to number of pixels on screen
WINDOW_HEIGHT = VERTICAL_PIXELS * PIXEL_SIZE
WINDOW_WIDTH = HORIZONTAL_PIXELS * PIXEL_SIZE

# Definition of Snake object, will hold all the properties of snake
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xspeed = PIXEL_SIZE
        self.yspeed = 0
        self.body = [(x, y)]
        
# Definition of Food Object, will hold position of food 
class Food:
    def __init__(self):
        self.x = PIXEL_SIZE * random.randint(0, HORIZONTAL_PIXELS - 1)
        self.y = PIXEL_SIZE * random.randint(0, VERTICAL_PIXELS - 1)
    
    def pick_new_location(self):
        self.x = PIXEL_SIZE * random.randint(0, HORIZONTAL_PIXELS - 1)
        self.y = PIXEL_SIZE * random.randint(0, VERTICAL_PIXELS - 1)

# Initialise PyGame
pygame.init()

# Create screen for showing viusalisation
size = width, height = WINDOW_WIDTH, WINDOW_HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")


# Create a surface on which we will draw our pixels
rect_canvas = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))

# Create Snake and Food Objects, spawn snake near center. Give Snake a cute name. THIS IS VERY IMPORTANT
Sneko = Snake((HORIZONTAL_PIXELS // 2) * PIXEL_SIZE, (VERTICAL_PIXELS // 2) * PIXEL_SIZE)
Nom = Food()

print(Nom.x, Nom.y)

# While game is running, for every frame,
while True:

    # Store events to process quit and KeyDown events
    events = pygame.event.get()

    for event in events:
        # Let user exit
        if event.type == pygame.QUIT: sys.exit()

        # Turn snake according to key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Sneko.xspeed = -PIXEL_SIZE
                Sneko.yspeed = 0
            if event.key == pygame.K_RIGHT:
                Sneko.xspeed = PIXEL_SIZE
                Sneko.yspeed = 0
            if event.key == pygame.K_DOWN:
                Sneko.yspeed = PIXEL_SIZE
                Sneko.xspeed = 0
            if event.key == pygame.K_UP:
                Sneko.yspeed = -PIXEL_SIZE
                Sneko.xspeed = 0

    # Fill the screen with black
    screen.fill(BLACK)

    # Move Snake head
    Sneko.x += Sneko.xspeed
    Sneko.y += Sneko.yspeed

    # Handle border cases where snake hits the border
    if (Sneko.x > (WINDOW_WIDTH - PIXEL_SIZE)):
        Sneko.x = 0
    if (Sneko.x < 0):
        Sneko.x = WINDOW_WIDTH - PIXEL_SIZE
    if (Sneko.y > (WINDOW_HEIGHT - PIXEL_SIZE)):
        Sneko.y = 0
    if (Sneko.y < 0):
        Sneko.y = WINDOW_HEIGHT - PIXEL_SIZE

    # Draw food object
    pygame.draw.rect(rect_canvas, FOOD_COLOR, pygame.Rect(0, 0,  PIXEL_SIZE, PIXEL_SIZE))
    screen.blit(rect_canvas, (Nom.x, Nom.y))

    # Move the body of the snake to follow the snake head
    for block_index in range(len(Sneko.body) - 1):
        Sneko.body[block_index] = Sneko.body[block_index + 1]
    Sneko.body[len(Sneko.body) - 1] = (Sneko.x, Sneko.y)

    # Check if Snake head has touched a part of it's body
    if (Sneko.x, Sneko.y) in Sneko.body[:-1]:
        Sneko.body = [(Sneko.x, Sneko.y)]

    # Draw every block in snake's body
    for block_pos in Sneko.body:
        pygame.draw.rect(rect_canvas, SNAKE_COLOR, pygame.Rect(0, 0,  PIXEL_SIZE, PIXEL_SIZE))
        screen.blit(rect_canvas, (block_pos[0], block_pos[1]))

    # If Snake head touches a food object, add new square to snake and move food
    if (Sneko.x == Nom.x) and (Sneko.y == Nom.y):
        Nom.pick_new_location()
        Sneko.body.append((Sneko.x, Sneko.y))

    # Update the display
    pygame.display.update()

    # Tick the display as per FPS
    pygame.time.Clock().tick(FPS)
    