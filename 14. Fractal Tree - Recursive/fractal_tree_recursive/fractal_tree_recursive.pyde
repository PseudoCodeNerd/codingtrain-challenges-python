# Angle constant
angle = PI/8

# Setup screen
def setup():
    size(400, 400)

# Draw root branch
def draw():
    background(0)
    stroke(255)
    translate(200, 400)
    branch(100)

# If branch is too small, don't draw it. Else, draw left and right branch
def branch(length):
    if length < 2:
        return
    line(0, 0, 0, -length)
    translate(0, -length)
    push()
    rotate(angle)
    branch(length*0.67)
    pop()
    push()
    rotate(-angle)
    branch(length*0.67)
    pop()
