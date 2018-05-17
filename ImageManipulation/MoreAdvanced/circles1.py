# Look at the code. What do you think it will draw?
# Run the code and then check you understand the code 

# Setup the turtle module 
import turtle

# create a graphics window
myScreen = turtle.Screen()

# create a new turtle called myTurtle
myTurtle = turtle.Turtle()

# The speed of the turtle can be changed 0-10
myTurtle.speed(0)

# set number of repeats and radius of circle
repeats = 50
radius = 5

# loop over range of numbers
for i in range(repeats):
    myTurtle.circle(radius*i)

# wait for mouseclick to close window
myScreen.exitonclick()  
