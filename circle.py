import turtle
screen=turtle.Screen()
pen=turtle.Turtle()

def drawCircle(x,y,r):
    pen.pu()
    pen.goto(x,y-r)
    pen.pd()
    pen.circle(r)


def makepicture(x,y,r):
    if r<10:
        drawCircle(x,y,r)
    else:
        drawCircle(x,y,r)
        makepicture()
makepicture(0,0,200)
turtle.done()