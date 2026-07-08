import turtle
import math

turtleWindow = turtle.Screen()
turtleWindow.title("Flower Drawing")
turtleWindow.bgcolor("light blue")
YOUR_NAME=turtle.Turtle("circle")
YOUR_NAME.speed(10)

def drawPetal(t, r, arcAngle, n, color):
# t is your turtle name
# r is petal height
# arcAngle is petal width

    for i in range(n):
        t.pencolor(color)
        t.pensize(10)
        t.forward((r*(arcAngle*(math.pi/180)))/n)
        t.left(arcAngle/n)
        
    t.left(180-arcAngle)
    
    for i in range(n):
        t.pencolor(color)
        t.pensize(10)
        t.forward((r*(arcAngle*(math.pi/180)))/n)
        t.left(arcAngle/n)

    t.left(180-arcAngle)
    
def drawStem(t, StemLength, bearing):
    
    t.setheading(bearing)
    t.pencolor("brown")
    t.pensize(5)
    t.forward(-StemLength)
    t.penup()
    t.home()
    t.pendown()
    t.setheading(0)

def drawFlower(t, numpetals, PetalHeight, PetalWidth, StemLength, color):
    
    drawStem(t, StemLength, 90)
    
    for i in range(numpetals):
        t.color(color)
        t.begin_fill()
        drawPetal(t, PetalHeight, PetalWidth, 100, color)
        t.left(360/numpetals)
        t.end_fill()

#SOME EXAMPLES
# drawFlower(YOUR_NAME, 5, 100, 90, 500, "pink")
#drawFlower(YOUR_NAME, 5, 50, 120, 500, "pink")

##turtle becomes centre of the flower -- edit to your turtle's name :)
YOUR_NAME.penup()
YOUR_NAME.home()
YOUR_NAME.color("yellow")

turtle.done()
