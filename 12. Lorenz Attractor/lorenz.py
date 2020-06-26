import pygame, sys, random
# Settings for Window Size
WINDOW_HEIGHT = 600
WINDOW_WIDTH =  900

SIGMA, RHO, BETA = 10, 28, 8/3

FPS = 1

WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("The Lorenz Attractor")

x, y, z = 0.01, 0, 0 
dt = 1e-2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0, 0, 0))

    dx = (SIGMA * (y - x)) * dt
    x += dx
    dy = (x * (RHO - z) - y) * dt
    y += dy
    dz = (x * y - BETA * z) * dt
    z += dz

    print(x, y, z)
    
    pygame.draw.circle(screen, WHITE, (int(x)+WINDOW_WIDTH//2, int(y)+WINDOW_HEIGHT//2), 0)
    # Update the display
    pygame.display.update()

    # Tick the display as per FPS
    pygame.time.Clock().tick(FPS)


