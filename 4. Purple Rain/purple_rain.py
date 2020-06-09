
# desc: In this coding challenge (originally done at The Coding Train), I attempt to code some dope looking Purple Rain in pygame.
# A part of Coding Train's Challenges implementation in Python series.
# @author: PseudoCodeNerd

import pygame
from random import randint, choice

# Settings for Window Size
WINDOW_HEIGHT = 600
WINDOW_WIDTH =  900

# Color constants 
PURPLE = (171, 32, 253)
BG = (230, 230, 250)

# OTHER VARIABLES
NUM_DROPS = 500
RAINY_DAY = True

# Create a 'Drop' class
class RainDrop:
    def __init__(self, surface, color, x, y, h, w, g):
        """
        Instantiate a drop of specified color on a surface
        params
        surface : surface to draw on
        color : color of the drop
        x : x-coordinate of the drop
        y : y-coordinate of the drop
        h : height of the individual drop
        w : width of the individual drop
        g : gravitation (force bringing the drop down)
        """
        self.surface = surface
        self.color = color
        self.x = x 
        self.y = y
        self.h = h
        self.w = w
        self.g = g
        # start at time = 0
        self.t = 0

    def fall(self):
        """
        Simulate falling of a rain-drop.
        params
        self : RainDrop Object
        """ 
        # we have to change the vertical position of each drop with time
        # Use Second Equation of Motion : Y = V_y*t + (g*t^2)/2
        self.y = int(self.y + (self.g * self.t**2)/2)
        # if drop goes out of window, reinitalize it somewhere on the screen
        if self.y > 700:
            self.y  = -1 * randint(300, 1200)
            # wait for some time after a batch of drops goes out of window
            self.t = 0.05
        self.t += 0.01
        # draw using pygame rect
        pygame.draw.rect(self.surface, self.color, [self.x, self.y, self.w, self.h])

# Instantiate a clock to keep track of time
clock = pygame.time.Clock()

# Create a surface for rainfall viusalisation
pygame.init()
rain_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Purple Rain")
pygame.display.update()

# Make the Rain-Drops on the screen
raindrops = []
widths = [w for w in range(1, 6)]
heights = [h for h in range(15, 48, 3)]
gravs = [g for g in range(1, 20, 5)]
params = list(zip(widths, heights, gravs))

#making the rain drops
for _ in range(NUM_DROPS):
    # randomize initial raindrop parameters
    x = randint(15, 885)
    y = -1 * randint(200 , 1400)
    w , h , g = choice(params) 
    raindrop = RainDrop(rain_screen ,PURPLE, x, y, h , w, g)  
    raindrops.append(raindrop)


# While the game is running, for every frame,
while RAINY_DAY:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RAINY_DAY = False  # :-(
     
    rain_screen.fill(BG)
        
    for rd in raindrops:
         # Make it RAIN!!
        rd.fall() 
    # Update the display       
    pygame.display.update()
    # Tick the display / clock
    clock.tick(80)

pygame.display.quit()
quit()

# FIN.