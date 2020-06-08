import pygame
import random
import sys

# Settings for Window size
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 1600

# Settings for the graphics
SIMULATION_DEPTH = 800
STAR_SIZE = 1
NUMBER_OF_STARS = 1200
FPS = 60
MOVEMENT_SPEED = 3

# Color constants
STAR_COLOR = 255, 255, 255
BLACK = 0, 0, 0

# Definition of Star object, will hold all the properties of star
class Star:
    def __init__(self, x, y, z, opacity):
        self.x = x
        self.y = y
        self.z = z
        self.opacity = opacity

# Variable substitutions used in code so that zooming is centered on center of window 
H = WINDOW_HEIGHT // 2
W = WINDOW_WIDTH // 2
D = SIMULATION_DEPTH // 2

# Generate stars at random places, and make a list of them
STAR_LIST = []
for i in range(NUMBER_OF_STARS):
    # Keep depth more than 1 so that there is no zero division error later for the zooming part
    depth = random.randrange(1, 2 * D)

    # Adjust the opacity such that the stars closest will be brightest, and the ones farthest are faintest
    depth_adjusted_opacity = int(255 * (1 - (depth / (2 * D))))

    # Add Star object to list
    STAR_LIST.append(Star(random.randrange(0, 2 * W), random.randrange(0, 2 * H), depth, depth_adjusted_opacity))

# Initialise PyGame
pygame.init()

# Create screen for showing viusalisation
size = width, height = 2 * W, 2 * H
screen = pygame.display.set_mode(size)

# Create a surface on which we will draw our star, make it allow transparency
circ = pygame.Surface((2 * STAR_SIZE, 2 * STAR_SIZE), pygame.SRCALPHA)

# While the game is running, for every frame,
while True:
    # Let user exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw every star, and calculate it's movement across screen
    for star in STAR_LIST:
        # New x and y for the moving star, depends on how far the star is from camera
        sx = int(((star.x - W)/star.z) * D)
        sy = int(((star.y - H)/star.z) * D)

        # Draw the star on the circle drawing surface with appropriate opacity and size at appropriate position
        pygame.draw.circle(circ, pygame.Color(*STAR_COLOR, min(star.opacity, 255)), (STAR_SIZE, STAR_SIZE), STAR_SIZE)
        
        # Blit the temporary circle surface onto the screen
        screen.blit(circ, (sx + W, sy + H))

        # Move star closer to camera
        star.z -= MOVEMENT_SPEED

        # Increase opacity of star
        star.opacity += 1

        # If the star is too close to camera or is outside the window, give it a new position
        if (star.z < 1) or (sx > W) or (sy > H)or (sx < -W) or (sy < -H):
            # Make sure star is transparent since it spawns at the farthes position from camera
            star.opacity = 0

            # Give it a new position
            star.x = random.randrange(0, 2 * W)
            star.y = random.randrange(0, 2 * H)
            star.z = 2 * D
            
    # Update the display
    pygame.display.update()

    # Tick the display as per FPS
    pygame.time.Clock().tick(FPS)
    