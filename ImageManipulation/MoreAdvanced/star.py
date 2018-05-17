# Python program to draw a star

# Load turtle module
import turtle

# Create a graphics window and set background colour
myScreen = turtle.Screen()
myScreen.bgcolor("lightgreen")

# Create new turtle called spiral
spiral = turtle.Turtle()

# Define variables
lines = 40
step  = 10
angle = 144

# Loop over range of numbers
for i in range(lines):
    spiral.forward(i * step)
    spiral.right(angle)

# Wait for mouseclick to close window
myScreen.exitonclick()
