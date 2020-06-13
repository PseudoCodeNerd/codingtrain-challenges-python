# Definition of Cell object, will hold all the properties of cell
class Cell:
    def __init__(self, row, col, walls, surface):
        """
        Create a cell
        params
        row : Row index of cell in 2D array
        col : Column index of cell in 2D array
        walls : List of booleans in the order [top, right, bottom, left] representing if the respective walls of that cell exist
        surface : Surface on which cell should be drawn
        """
        self.row = row
        self.col = col
        self.walls = walls
        self.surface = surface
    def show(self):
        """
        Draws each cell, according to if it's visited, and drwas each wall (if the wall exists)
        """
        pygame.draw.rect(self.surface, CELL_COLOR, pygame.Rect(self.col * CELL_WIDTH, self.row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

        if self.walls[0]:
            pygame.draw.line(self.surface, WALL_COLOR, (self.col * CELL_WIDTH, self.row * CELL_HEIGHT), ((self.col + 1) * CELL_WIDTH, self.row * CELL_HEIGHT))
        if self.walls[1]:
            pygame.draw.line(self.surface, WALL_COLOR, ((self.col + 1) * CELL_WIDTH, self.row * CELL_HEIGHT), ((self.col + 1) * CELL_WIDTH, (self.row + 1) * CELL_HEIGHT))
        if self.walls[2]:
            pygame.draw.line(self.surface, WALL_COLOR, ((self.col + 1) * CELL_WIDTH, (self.row + 1) * CELL_HEIGHT), (self.col * CELL_WIDTH, (self.row + 1) * CELL_HEIGHT))
        if self.walls[3]:
            pygame.draw.line(self.surface, WALL_COLOR, (self.col * CELL_WIDTH, (self.row + 1) * CELL_HEIGHT), (self.col * CELL_WIDTH, self.row * CELL_HEIGHT))

if __name__ == "__main__":
    import pygame
    import random
    import sys

    # Set for Window size
    HORIZONTAL_BLOCKS = 32
    VERTICAL_BLOCKS = 18

    CELL_WIDTH = 50
    CELL_HEIGHT = 50
    
    # Set FPS
    FPS = 60

    # Color constants
    CELL_COLOR = 255, 255, 255
    WALL_COLOR = 0, 0, 0
    BG_COLOR = 0, 0, 0

    # Initialise PyGame
    pygame.init()

    # Create screen for showing viusalisation
    size = width, height = HORIZONTAL_BLOCKS * CELL_HEIGHT, VERTICAL_BLOCKS * CELL_HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Maze Generator")

    # Create a 1D list of cells, and append cells to it
    cells = []

    for i in range(VERTICAL_BLOCKS):
        for j in range(HORIZONTAL_BLOCKS):
            cells.append(Cell(i, j, [True, True, True, True], screen))

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

        # Show every cell
        for k in cells:
            k.show()

        # Update the display
        pygame.display.update()

        # Tick the display as per FPS
        pygame.time.Clock().tick(FPS)
        