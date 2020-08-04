# Definition of Branch object, will hold all the properties of branch
class Branch:
    def __init__(self, start, end, surface, angle, relative_orientation):
        """
        Create a branch
        params
        start : The start point (tuple) of the branch
        end : The end point (tuple) of the branch
        surface : Surface on which branch should be drawn
        angle : Global angle of the branch w.r.t. y-axis. Anticlockwise is negative, clockwise is positive
        relatice_orientation : Orientation of the branch w.r.t. its parent branch. 1 for right, -1 for left
        """
        self.start = start
        self.end = end
        self.surface = surface
        self.angle = angle
        self.relative_orientation = relative_orientation

    # Make the branch show itself
    def show(self):
        pygame.draw.line(self.surface, LINE_COLOR, self.start, self.end)

    # Create a right branch
    def branch_r(self):
        length = math.dist(self.start, self.end)
        if self.relative_orientation:
            right = Branch(self.end, (self.end[0] + length * LENGTH_MULTIPLIER * math.sin(self.angle + ANGLE), self.end[1] - length * LENGTH_MULTIPLIER * math.cos(self.angle + ANGLE)), self.surface, self.angle + ANGLE, 1)
        else:
            right = Branch(self.end, (self.end[0] + length * LENGTH_MULTIPLIER * math.sin(self.angle + ANGLE), self.end[1] - length * LENGTH_MULTIPLIER * math.cos(self.angle + ANGLE)), self.surface, self.angle - ANGLE, 1)
        return right

    # Create a left branch
    def branch_l(self):
        length = math.dist(self.start, self.end)
        if self.relative_orientation:
            left = Branch(self.end, (self.end[0] + length * LENGTH_MULTIPLIER * math.sin(self.angle - ANGLE), self.end[1] - length * LENGTH_MULTIPLIER * math.cos(self.angle - ANGLE)), self.surface, self.angle - ANGLE, -1)
        else:
            left = Branch(self.end, (self.end[0] + length * LENGTH_MULTIPLIER * math.sin(self.angle - ANGLE), self.end[1] - length * LENGTH_MULTIPLIER * math.cos(self.angle - ANGLE)), self.surface, self.angle + ANGLE, -1)
        return left

if __name__ == "__main__":
    import pygame
    import random
    import sys
    import math
    
    # Set FPS
    FPS = 60

    # Color constants
    LINE_COLOR = 255, 255, 255
    BG_COLOR = 0, 0, 0

    # Tree constants
    LENGTH_MULTIPLIER = 0.67
    ANGLE = math.pi/8

    # Initialise PyGame
    pygame.init()

    # Create screen for showing viusalisation
    size = width, height = (400, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Fractal Tree - OOP")

    # Create an array that will hold all the branches
    tree = []

    # Create a root branch
    root = Branch((width/2, height), (width/2, height - 100), screen, 0, 1)
    tree.append(root)

    # While game is running, for every frame,
    while True:
        # Store events to process quit and KeyDown events
        events = pygame.event.get()

        # Handle exit event
        for event in events:
            # Let user exit
            if event.type == pygame.QUIT: sys.exit()

            # If space key is pressed, generate a new level of branches
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for index in range(len(tree)-1, -1, -1):
                        tree.append(tree[index].branch_r())
                        tree.append(tree[index].branch_l())

        # Fill the screen with BG_COLOR
        screen.fill(BG_COLOR)

        # Show every branch
        for branch in tree:
            branch.show()

        # Update the display
        pygame.display.update()

        # Tick the display as per FPS
        pygame.time.Clock().tick(FPS)
        