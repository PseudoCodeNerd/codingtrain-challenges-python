# Definition of Cell object, will hold all the properties of cell
class Cell:
    def __init__(self, a, b, surface):
        """
        Create a cell
        params
        a : Amount of chemical A
        b : Amount of chemical B
        surface : Surface on which cell should be drawn
        """
        self.a = a
        self.b = b
        
if __name__ == "__main__":
    import pygame
    import random
    import sys
    
    # Set FPS
    FPS = 120
    
    # Some constants for the Gray-Scott Model
    D_A = 1
    D_B = 0.5
    FEED = 0.055
    KILL = 0.062

    # Initialise PyGame
    pygame.init()

    # Create screen for showing viusalisation
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Reaction Diffusion Simulator")

    # Create two timeframes for last frame and current frame
    grid = [[Cell(1, 0, screen) for i in range(100)] for j in range(100)]
    next = [[Cell(1, 0, screen) for i in range(100)] for j in range(100)]

    # Fill center with chemical B
    for i in range(40, 60):
        for j in range(40, 60):
            grid[i][j].b = 1

    # Apply convolution and return result of convolution. Probably should do this with numpy
    def laplace(grid, x, y):
        s_a = grid[x][y].a * -1
        s_a += grid[x-1][y].a * 0.2
        s_a += grid[x+1][y].a * 0.2
        s_a += grid[x][y-1].a * 0.2
        s_a += grid[x][y+1].a * 0.2
        s_a += grid[x-1][y-1].a * 0.05
        s_a += grid[x-1][y+1].a * 0.05
        s_a += grid[x+1][y-1].a * 0.05
        s_a += grid[x+1][y+1].a * 0.05

        
        s_b = grid[x][y].b * -1
        s_b += grid[x-1][y].b * 0.2
        s_b += grid[x+1][y].b * 0.2
        s_b += grid[x][y-1].b * 0.2
        s_b += grid[x][y+1].b * 0.2
        s_b += grid[x-1][y-1].b * 0.05
        s_b += grid[x-1][y+1].b * 0.05
        s_b += grid[x+1][y-1].b * 0.05
        s_b += grid[x+1][y+1].b * 0.05
        return s_a, s_b

    # While game is running, for every frame,
    while True:
        # Store events to process quit and KeyDown events
        events = pygame.event.get()

        # Handle exit event
        for event in events:
            # Let user exit
            if event.type == pygame.QUIT: sys.exit()

        # Fill the screen with BG_COLOR
        screen.fill(BG_COLOR)
        
        # For every pixel,
        for cell_row_index in range(1, len(next)-1):
            for cell_index in range(1, len(next[cell_row_index])-1):
                # Calculate new value of pixel according to Gray-Scott Model
                a = grid[cell_row_index][cell_index].a
                b = grid[cell_row_index][cell_index].b
                laplace_sum = laplace(grid, cell_row_index, cell_index)
                next[cell_row_index][cell_index].a = a + (D_A * laplace_sum[0]) - (a * b * b) + (FEED * (1 - a))
                next[cell_row_index][cell_index].b = b + (D_B * laplace_sum[1]) + (a * b * b) - ((KILL + FEED) * b)
                # Constrain Values
                next[cell_row_index][cell_index].a = max(0, min(1, next[cell_row_index][cell_index].a))
                next[cell_row_index][cell_index].b = max(0, min(1, next[cell_row_index][cell_index].b))
        # For every pixel,
        for cell_row_index, cell_row in enumerate(grid):
            for cell_index, cell in enumerate(cell_row):
                # Render the pixel according to its value
                temp = pygame.Surface((4, 4), pygame.SRCALPHA)
                color = max(0, min((int(cell.a*255) - int(cell.b*255)), 255))
                pygame.draw.rect(temp, (color, color, color, 255), pygame.Rect(0, 0, 4, 4))
                screen.blit(temp, (cell_index*4, cell_row_index*4))
        # Swap the next and previous grid so that new grid can be calculated
        temp = grid
        grid = next
        next = temp
        # Update the display
        pygame.display.update()
        # Tick the display as per FPS
        pygame.time.Clock().tick(FPS)
