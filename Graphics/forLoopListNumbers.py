# For loops
# Repeat a set of instructions using a for loop
# Loop over a list of numbers

# Setup the turtle module
import turtle

# Create a graphics window
myScreen = turtle.Screen()

# Create new Turtle called mockTurtle
mockTurtle = turtle.Turtle()

# Make list of colors
penwidths = [5,10,15,20]

# Loop over list
for penwidth in penwidths:
    mockTurtle.pensize(penwidth)
    mockTurtle.forward(100)
    mockTurtle.left(90)

# Wait for mouseclick to close window
myScreen.exitonclick()
