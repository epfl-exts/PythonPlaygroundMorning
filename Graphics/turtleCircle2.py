# Python program to draw a circle
# One way to draw a circle is to draw many short staright lines (see turtleCircle.py)
# Another way of drawing a circle with turtle is to use a predefined motion type

# Setup the turtle module
import turtle

# Create a graphics window
window = turtle.Screen()

# Create a new turtle called myTurtle
myTurtle = turtle.Turtle()

# Circle motion requires a radius to be defined
radius = 40
myTurtle.circle(radius)

# Wait for mouseclick to close window
window.exitonclick()
