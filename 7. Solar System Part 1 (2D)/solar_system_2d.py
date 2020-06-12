# Definition of Planet object, will hold all the properties of planet
class Planet:

    # 
    def __init__(self, radius, mass, distance, parent, level, glob_surface):
        self.radius = radius
        self.mass = radius
        self.distance = distance
        self.parent = parent
        self.level = level
        self.children = []
        self.global_surface = glob_surface

        # If the planet is not a universal parent, don't rotate it. Else, use the orbital angular velocity formula
        # NOTE: The value of G is changed in this context to make the rotation faster than actual life values
        if self.parent:
            self.s = (6.67 * 2 * math.pi * (10**2) * self.parent.mass) / (self.distance.length() ** 3)
        else:
            self.s = 0

    def draw(self):
        # Make a planet canvas on which we'll draw our planets. Make sure to enable opacity
        planet_canvas = pygame.Surface((400, 400), pygame.SRCALPHA)
        # Draw planet onto the global screen
        pygame.draw.circle(planet_canvas, (*PLANET_COLOR, 100), (self.radius, self.radius), self.radius)
        # Draw the planet at the right position by getting the net position vector with respect to universal parent planet (center of world)
        self.global_surface.blit(planet_canvas, (HORIZONTAL_PIXELS // 2 + self.get_net_pos()[0] - self.radius, VERTICAL_PIXELS // 2 + self.get_net_pos()[1] - self.radius))
        
        if self.parent:
            # If the planet has a parent, draw a line from the center of the parent's center to this planet's center
            pygame.draw.line(self.global_surface, (*PLANET_COLOR, 255), (HORIZONTAL_PIXELS // 2 + self.parent.get_net_pos()[0], VERTICAL_PIXELS // 2 + self.parent.get_net_pos()[1]), (HORIZONTAL_PIXELS // 2 + self.get_net_pos()[0], VERTICAL_PIXELS // 2 + self.get_net_pos()[1]))
        
        # Draw its children
        for i in self.children:
            i.draw()

    # Rotate every planet by angular orbit velocity, and draw the system again
    def orbit(self):
        self.distance.rotate_ip(self.s)
        self.draw()
        for i in self.children:
            i.orbit()

    # Create number of children
    def spawn_children(self, number):
        for i in range(number):
            # Set mass to a random value
            mass = random.randrange(1, 100)
            
            # Limit radius to parent's radius, but don't make it too small
            rad = random.randrange(self.radius // 4 + 1, self.radius)

            # Generate random polar vector from parent panet to the new one
            distance = random.randrange(self.radius + rad, int((self.radius + rad)*1.5))
            angle = random.random() * 2 * math.pi
            x = pygame.Vector2()
            x.from_polar((distance, angle * (180/math.pi)))
            
            # Instantiate child with calculated properties
            self.children.append(Planet(rad, mass, x, self, self.level + 1, self.global_surface))

    # Get net position vector with respect to the center of the world
    def get_net_pos(self):
        net_dir = pygame.Vector2()
        if self.parent:
            net_dir = self.distance + self.parent.get_net_pos()
        return net_dir

if __name__ == "__main__":
    import pygame
    import random
    import sys
    import math

    # Settings for Window size
    HORIZONTAL_PIXELS = 1920
    VERTICAL_PIXELS = 1000
    
    # Settings for the graphics
    FPS = 60

    # Color constants
    PLANET_COLOR = 255, 255, 255
    BG_COLOR = 0, 0, 0

    # Initialise PyGame
    pygame.init()

    # Create screen for showing viusalisation
    size = width, height = HORIZONTAL_PIXELS, VERTICAL_PIXELS
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Solar System 2D")

    # Create a surface on which we will draw our objects, enable opacity
    planet_canvas = pygame.Surface((400, 400), pygame.SRCALPHA)

    # Create a Sun or universal parent planet
    System = Planet(100, 100, pygame.Vector2(), None, 0, screen)

    # Spawn multiple levels of children
    System.spawn_children(random.randrange(1, 3))
    for planet in System.children:
        planet.spawn_children(random.randrange(1, 3))
        for planet_children in planet.children:
            planet_children.spawn_children(random.randrange(1, 3))

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

        # Draw the system, and update it
        System.draw()
        System.orbit()


        # Update the display
        pygame.display.update()

        # Tick the display as per FPS
        pygame.time.Clock().tick(FPS)
        