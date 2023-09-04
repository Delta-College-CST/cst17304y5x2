# This program draws shapes (square, triangle, rectangle) with random
# positions, dimensions, and colors.

import turtle

import random

# Set up the screen
screen = turtle.Screen()

# Select random numbers for random background color
colorCode = random.randint(1, 3)
if colorCode == 1:
    screen.bgcolor("red")
elif colorCode == 2:
    screen.bgcolor("blue")
else:
    screen.bgcolor("green")

# Create a turtle object
pen = turtle.Turtle()

# Select random position for shape and ready pen
xPos      = random.randint(-200,200)
yPos      = random.randint(-200,200)
pen.penup()
pen.goto(xPos,yPos)
pen.pendown()

# Select random numbers for random pen color
colorCode = random.randint(1, 5)
if colorCode == 1:
    pen.pencolor("black")
elif colorCode == 2:
    pen.pencolor("white")
elif colorCode == 3:
    pen.pencolor("purple")
elif colorCode == 4:
    pen.pencolor("cyan")
else:
    pen.pencolor("brown")

shapeChoice = random.randint(1,3)     # Randomly select shape

if shapeChoice == 1:                  # Draw a square
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)

if shapeChoice == 2:                  # Draw an equilateral triangle
    pen.pendown()
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)

if shapeChoice == 3:                  # Draw a rectangle
    length = random.randint(50,300)    
    width  = random.randint(50,300)   # Randomize length and width
    pen.pendown()
    pen.goto(xPos+width, yPos)
    pen.goto(xPos+width, yPos-length)
    pen.goto(xPos, yPos-length)
    pen.goto(xPos, yPos)


