# desc: In this coding challenge (originally done at the Coding Trains), I attempt to code a Lorenz Attractor using Processing | Python.
# A part of Coding Train's Challenges implementation in Python series.
# @author: PseudoCodeNerd


# Setting global variables
WINDOW_HEIGHT = 600
WINDOW_WIDTH =  800

# direct from the wiki page on Lorenz Attractors
SIGMA, RHO, BETA = 10, 28, 8/3

# give starting vars to start calculating derivatives
x, y, z = 0.1, 0.1, 0.1 
rotatn_angle = 0

# keep track of prev points
pts = []


# setup scene
def setup():
    size(WINDOW_WIDTH, WINDOW_HEIGHT, P3D)
    colorMode(HSB)
    

def draw():
    global x, y, z, SIGMA, RHO, BETA, pts, rotatn_angle
    background(0)

    # trial and error to demonstrate smol passage of time
    dt = 1e-2

    # formulas too straight outta wikipedia
    dx = (SIGMA * (y - x)) * dt
    x += dx
    dy = (x * (RHO - z) - y) * dt
    y += dy
    dz = (x * y - BETA * z) * dt
    z += dz
    
    pts.append(PVector(x, y, z))
    
    # screen mutations
    translate(width/2, height/2)
    scale(5)
    stroke(255)
    noFill()

    # rotate
    rotateY(rotatn_angle*0.5)
    rotateX(rotatn_angle*0.8)
    rotatn_angle += 0.01
    
    hue_v = 0
    beginShape()
    for pt in pts:
        stroke(hue_v, 255, 255)
        vertex(pt.x, pt.y, pt.z)
        hue_v += 1.5
        # reinitialize colors
        if hue_v >= 255:
            hue_v = 0
    endShape()