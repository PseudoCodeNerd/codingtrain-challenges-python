# desc: In this coding challenge (originally done at the Coding Trains), I attempt to code the Menger Sponge (fractals) using Processing | Python.
# A part of Coding Train's Challenges implementation in Python series.
# @author: PseudoCodeNerd

# Setting global variables / preferences
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1200
SPONGE_COLOR = '#81ecec'
BG_COLOR = '#2d3436'
SPONGE_SIZE = 300
sponge_lis = list()
rotatn_angle = 0


# The 'BOX' class.
class Box():
    # constructor (init func)
    def __init__(self, x, y, z, s):
        """
        Constructs a box
        
        params
        x, y, z  : coords of the box
        s : size (of side) of the box
        """
        self.posn = PVector(x, y, z)
        self.s = s
        
    def show(self):
        """
        Shows a box with specified SPONGE_COLOR and SPONGE_SIZE)
        """
        pushMatrix()
        translate(self.posn.x, self.posn.y, self.posn.z)
        noStroke()
        fill(SPONGE_COLOR)
        box(self.s)
        popMatrix()
    
    def takeStep(self):
        """
        Takes a box, chop it into small boxes, remove all center sub-boxes from each box.
        """
        boxes = list()
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    coordSum = abs(x) + abs(y) + abs(z)
                    new_s = float(self.s / 3)
                    if coordSum > 1:
                        new_box = Box(self.posn.x + x * new_s, self.posn.y + y * new_s, self.posn.z + z * new_s, new_s)
                        boxes.append(new_box)
        return boxes
        
# setup scene
def setup():
    # use P3D renderer for 3D object
    size(WINDOW_WIDTH, WINDOW_HEIGHT, P3D)
    initBox = Box(0, 0, 0, SPONGE_SIZE)
    sponge_lis.append(initBox)

# see name of the function to see what it does
def draw():
    global rotatn_angle
    background(BG_COLOR)
    # center the cube
    translate(width/2, height/2)
    noFill()
    lights()
    # rotating the cube
    rotateY(rotatn_angle*0.4)
    rotateX(rotatn_angle*0.8)
    rotatn_angle += 0.02
    # show boxes
    for box_ in sponge_lis:
        box_.show()
        
# Create new generation on click of mouse button
def mousePressed():
    global sponge_lis
    # save every next generation in the list below
    new_sponge_lis = list() 
    
    # run takeStep on each box
    for _box in sponge_lis:
        next_step = _box.takeStep()
        for new_box in next_step:
            new_sponge_lis.append(new_box)
    
    sponge_lis = new_sponge_lis