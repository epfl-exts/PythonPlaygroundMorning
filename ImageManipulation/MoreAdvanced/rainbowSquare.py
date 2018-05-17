# Python program to draw rainbow square

import turtle

# create a graphics window and set background colour
myScreen = turtle.Screen()       
myScreen.bgcolor("lightblue")

# create a new turtle and define its speed
myTurtle = turtle.Turtle()
myTurtle.speed(0)

# define list of colours
colours = ['red', 'blue', 'purple', 'green']

angle = 90

# loop over the list of strings
for x in colours:
    myTurtle.color(x)
    myTurtle.forward(100)
    myTurtle.left(angle)

# wait for mouseclick to close window
myScreen.exitonclick()  
