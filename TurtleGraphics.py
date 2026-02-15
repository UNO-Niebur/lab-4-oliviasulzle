#TurtleGraphics.py
#Name: Olivia Sulzle
#Date: 2/15/25
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
 
def fillCorner(alice, corner):
    drawSquare(alice, 100)
   
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    elif corner == 3:
        alice.penup()
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.pendown()
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 4:
        alice.penup()
        alice.forward(50)
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.pendown()
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
        

def squaresInSquares(turtle, num):
        size = 200
        offset = 20
        for i in range(num):
            turtle.penup()
            turtle.goto((-size/2), (size /2))
            turtle.setheading(0)
            turtle.pendown()
            drawSquare(turtle, size)
            turtle.penup()
            turtle.forward(offset)
            turtle.right(90)
            turtle.forward(offset)
            turtle.left(90)
            turtle.pendown()
            size = size - (2 * offset)

def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
