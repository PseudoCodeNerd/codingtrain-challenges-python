angle = PI/8

def setup():
    size(400, 400)

def draw():
    background(0)
    stroke(255)
    translate(200, 400)
    branch(100)

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
