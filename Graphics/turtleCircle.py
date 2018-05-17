# Python program to draw a circle
# One way to draw a circle is to draw many short staright lines

# Run the program by typing in the terminal window
# python turtleCircle.py

# Setup the turtle module
import turtle

# Create a graphics window
window = turtle.Screen()

# Create a new turtle called myTurtle
myTurtle = turtle.Turtle()

# Repeat a set of instructions using a for loop
# Turtle moves forward 20 steps then turns 10 degrees. Then repeats 36 times.
repeats = 36
step = 20
angle = 10

# Loop over a range of numbers
for x in range (repeats):
    myTurtle.forward(step)
    myTurtle.right(angle)

# Wait for mouseclick to close window
window.exitonclick()
