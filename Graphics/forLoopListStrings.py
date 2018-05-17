# For loops
# Repeat a set of instructions using a for loop
# Loop over a list of strings

# Setup the turtle module
import turtle

# Create a graphics window
myScreen = turtle.Screen()

# Create new Turtle called mockTurtle
mockTurtle = turtle.Turtle()

# Make list of colors
colors = ['blue','green','hotpink']

# Loop over list
for color in colors:
    mockTurtle.pencolor(color)
    mockTurtle.forward(100)
    mockTurtle.left(120)

# Wait for mouseclick to close window
myScreen.exitonclick()
