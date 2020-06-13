# desc: In this coding challenge (originally done at The Coding Train), I attempt to code a mitosis simulation in pygame.
# A part of Coding Train's Challenges implementation in Python series.
# @author: PseudoCodeNerd

# Importing libraries
import pygame, sys, random, math
from pygame import gfxdraw

# Setting screen dimensions
WINDOW_HEIGHT = 600
WINDOW_WIDTH =  900

# Set FPS
FPS = 60

# Definition of Cell object, contains all properties of a single cell.
class Cell:
    def __init__(self, surface):
        self.surface = surface
        # Assign random color and position.
        self.color = (random.randint(155, 255), 0, random.randint(155, 255), 200)
        self.x = random.randint(50, 850)
        self.y = random.randint(50, 550)
        self.r = WINDOW_WIDTH//20
        
    def move(self):
        """
        Randomly move a cell on the screen, prevent it from going outside.
        """
        if random.random() < 0.5:
            vel = (random.uniform(0, 2), random.uniform(0, 2))
            self.x = math.floor(self.x - vel[0])
            self.y = math.floor(self.y - vel[1])
        else:
            vel = (random.uniform(0, 2), random.uniform(0, 2))
            self.x = math.floor(self.x + vel[0])
            self.y = math.floor(self.y + vel[1])
        if not 0<=self.x<WINDOW_WIDTH-self.r:
            self.x = random.randint(50, 850)
        if not 0<=self.y<WINDOW_HEIGHT-self.r:
            self.y = random.randint(50, 550)
    
    def clicked(self, m_x, m_y):
        """
        Checks if mouse clicked on a cell object.
        params
        m_x: x_coord of mouse click
        m_y : y_coord of mouse click
        return
        boolean: if click on cell object or not
        """
        d = math.sqrt((self.x - m_x)**2 + (self.y - m_y)**2)
        return d <= self.r

    def show(self):
        """
        Render a Cell on the screeen.
        """
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r)

    def mitosis(self, surface):
        """
        Creates two children cells from the parent cell (read up Mitosis please)
        params
        surface for the children cells
        """
        cell_a = Cell(surface)
        # Spawn the children close to the parent's location
        cell_a.x = self.x + self.r//2
        cell_a.y = self.y + (2 * self.r//2)
        cell_a.color = (random.randint(155, 255), 0, random.randint(155, 255), 200)
        cell_a.r = math.ceil(self.r * 0.9)

        cell_b = Cell(surface)
        cell_b.x = self.x + self.r//2
        cell_b.y = self.y
        cell_b.color = (random.randint(155, 255), 0, random.randint(155, 255), 200)
        cell_b.r = math.ceil(self.r * 0.96)

        return cell_a, cell_b


# Definition of Cells object. Cells represent all the individual cells on a screen in a list.
# Contains helper functions for mitosis.
class Cells:
    # Initialize Cells with one parent cell.
    def __init__(self, Cell_1):  
        cell_lis = []
        self.cell_lis = cell_lis
        self.Cell = cell
        cell_lis.append(cell)

    def num_cells(self):
        """
        get number of cells on the board
        """
        return len(self.cell_lis)

    def get_cell_lis(self):
        """
        get list of all cells on the board
        """
        return self.cell_lis

    def cell_clicked(self, surface, m_coords):
        """
        Perform mitosis
        params
        surface : board surface where cels reside
        m_coords : mouse-click coordinates
        """
        # Loops through all cells in decreasing order
        for i in range(len(self.cell_lis)-1, -1, -1):
            # call `clicked` to perform mitosis if mouse click on a cell
            if self.cell_lis[i].clicked(m_coords[0], m_coords[1]):
                # Get children cells
                cell_a, cell_b = self.cell_lis[i].mitosis(surface)
                self.cell_lis.append(cell_a)
                self.cell_lis.append(cell_b)
                # Remove parent cell
                self.cell_lis.remove(self.cell_lis[i])


# Initialize pygame
pygame.init()

# Create screen for showing simulation and set font for cell counter
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mitosis Simulation")
text = pygame.font.SysFont("Tahoma", 18)

# Initialize parent cell and Cells object
cell = Cell(surface)
Cells = Cells(cell)


# While game is running, for every frame,
while True:
    
    # Check for events
    for event in pygame.event.get():
        # If mouse click on a cell, perform mitosis
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Cells.cell_clicked(surface, pygame.mouse.get_pos())
        # Let user exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    s = Cells.num_cells()
    # Color the screen black
    surface.fill((0, 0, 0))
    # Keep track of cells on a counter
    counter = text.render("No. of Cells: {0}".format(s), 1, (255,255,255))
    surface.blit(counter, (5, 10))

    # Get *updated* cell_lis with every iteration
    cell_lis = Cells.get_cell_lis()
    #  Draw cells and move them
    for cell in cell_lis:
        cell.show()
        cell.move()

    # Update the display
    pygame.display.update()
    # Tick the display as per FPS
    pygame.time.Clock().tick(FPS)
