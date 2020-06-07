# Spirals made by the Thegr8kabeer
# Follow me on GitHub at https://github.com/thegr8kabeer
# Simple code for beginners by using 'Turtle' to create first project in less than 10 minutes
# Follow me on instagram at https://www.instagram.com/thegr8kabeer/



# -------------------- IMPORTING THE NECESSARY MODULES -----------------------

# For the spirals to work
import turtle

# For using some functions of the Python 'math' module.
import math

# For genrating random Spirals
import random

# --------------------- WRITING THE ACTUAL CODE -------------------------------

# declaring the screen as variable 'wn'
wn = turtle.Screen()

# Giving the screen the background color of 'black' (You can also modify the background color)
wn.bgcolor('black')

# Making the first spiral
First_spiral = turtle.Turtle()

# Setting the speed of the spiral as 0 (You can also modify the speed of the spiral of your choice)
First_spiral.speed(0)

# Giving the spiral a color of 'white' ( You can also modify the color of the spiral of your choice)
First_spiral.color('white')

# rotating the spiral at 360 degrees
rotate=int(360)

# Declaring a function for drawing the circles  
def drawCircles(t,size):
    
    # We want to draw the circles 10 times
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(First_spiral,100,10)

# Making the second spiral
second_spiral = turtle.Turtle()

# Setting the speed of the spiral as 0 (You can also modify the speed of the spiral of your choice)
second_spiral.speed(0)


# Giving the spiral a color of 'yellow' ( You can also modify the color of the spiral of your choice)
second_spiral.color('yellow')

# rotating the spiral at 90 degrees
rotate=int(90)

# Declaring a function for drawing the circles 
def drawCircles(t,size):
    
    # We want the circle to be made 4 times
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(second_spiral,100,10)

# Making the third spiral
third_spiral = turtle.Turtle()

# Setting the speed of the spiral as 0 (You can also modify the speed of the spiral of your choice)
third_spiral.speed(0)

# Giving the spiral a color of 'blue' ( You can also modify the color of the spiral of your choice)
third_spiral.color('blue')

# rotating the spiral at 80 degrees
rotate=int(80)

# Declaring a function for drawing the circles
def drawCircles(t,size):
    
    # We want the circle to be made 4 times
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(third_spiral,100,10)

# Making the fourth spiral
fourth_spiral = turtle.Turtle()

# Setting the speed of the spiral as 0 (You can also modify the speed of the spiral of your choice)
fourth_spiral.speed(0)

# Giving the spiral a color of 'white' ( You can also modify the color of the spiral of your choice)
fourth_spiral.color('orange')

# rotating the spiral at 90 degrees
rotate=int(90)

# Declaring a function for drawing the circles
def drawCircles(t,size):
    
    # We want the circle to be made 4 times
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(fourth_spiral,100,10)

# Making the fifth spiral
fifth_spiral = turtle.Turtle()

# Setting the speed of the spiral as 0 (You can also modify the speed of the spiral of your choice)
fifth_spiral.speed(0)

# Giving the spiral a color of 'white' ( You can also modify the color of the spiral of your choice)
fifth_spiral.color('pink')

# rotating the spiral at 90 degrees
rotate=int(90)

# Declaring a function for drawing the circles
def drawCircles(t,size):
    
    # We want to draw the circles 4 times
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(fifth_spiral,100,10)


# Feel free to modify my code.
# Don't forget to follow me.
# Happy Coding!