# Python program to draw series of squares
# Look at the code and predict what will be drawn.
# Run the code with 'python squares2.py'

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
# Increase length of side of square
length_increase = 6

# Increase number of repeats
repeats = 75

# Loop over range of numbers
for i in range (repeats):
  myTurtle.forward(side_length)
  myTurtle.left(angle)

  # Each repeat, increase the length of the side
  side_length = side_length + length_increase

# wait for mouseclick to close window
myScreen.exitonclick()
