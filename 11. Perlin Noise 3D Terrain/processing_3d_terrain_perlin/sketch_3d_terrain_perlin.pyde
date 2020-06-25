# desc: In this coding challenge (originally done at the Coding Trains), I attempt to code a 3D Terrain Using Perlin Noise in Processing | Python.
# A part of Coding Train's Challenges implementation in Python series.
# @author: PseudoCodeNerd

# Setting global vars
WINDOW_WIDTH = 2000
WINDOW_HEIGHT = 1600
SCALE = 20
f = 1

cols = WINDOW_WIDTH/SCALE
rows = WINDOW_HEIGHT/SCALE
# List of lists to hold heigt of each hill
terrain = [[0 for r in range(rows)] for c in range(cols)]


# setup scene
def setup():
    # use P3D renderer for 3D object
    size(1200, 800, P3D)


# see name of the function to see what it does
def draw():
    global terrain, cols, rows, w, h, SCALE, f
    f -= 0.1
    yoff = f
    # loop to create those animations
    for r in range(rows):
        xoff = 0
        for c in range(cols):
            # use processing's noise function to create natural random animations
            terrain[c][r] = map(noise(xoff, yoff), 0, 1, -100, 100)
            xoff += 0.2
        yoff += 0.2

    # setting up background
    background(0)
    stroke(255)
    noFill()
    translate(width/2, height/2+50)
    # give the mesh a 3d look
    rotateX(PI/3)
    translate(-w/2, -h/2)

    # setup mesh of triangles
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*SCALE, y*SCALE, terrain[x][y])
            vertex(x*SCALE, (y+1)*SCALE, terrain[x][y+1])
        endShape()
