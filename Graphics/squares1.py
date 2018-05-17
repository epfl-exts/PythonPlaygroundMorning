# Python program to draw a square
# Run the code with 'python squares1.py'

# Setup the turtle module
import turtle

# Create a graphics window
myScreen = turtle.Screen()

# Create a new turtle called myTurtle
myTurtle = turtle.Turtle()

# Set speed of the turtle
myTurtle.speed(10)

# Set colour of the turtle
myTurtle.color("magenta")

# Define variables
side_length=20
angle = 90
repeats = 4

# Loop over range of numbers
for i in range (repeats):
  myTurtle.forward(side_length)
  myTurtle.left(angle)

# Wait for mouseclick to close window
myScreen.exitonclick()
