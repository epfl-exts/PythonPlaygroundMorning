# Python program to draw series of squares
# The angle that the turtle turns has been changed.
# Predict what the turtle will now draw.
# Run the code with 'python squares3.py'

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
angle = 92
repeats = 75

length_increase = 6

# Loop over range of numbers
for i in range (repeats):
  myTurtle.forward(side_length)
  myTurtle.left(angle)
  side_length = side_length + length_increase

# Wait for mouseclick to close window
myScreen.exitonclick()
