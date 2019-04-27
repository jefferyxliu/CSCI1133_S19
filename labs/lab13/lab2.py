# CSCI 1133, Lab Section 013, lab13 Jeffery Liu, Random Colors, Shape Class, Circle Class, Graphics Display

import random

import turtle
myt = turtle.Turtle()
scr = turtle.Screen()
scr.delay(0)
myt.speed(0)
myt.hideturtle()



def randColor():
    return random.choice(["red", "yellow", "green", "blue", "purple", "orange"])

class Shape:
    def __init__(self, x = 0, y = 0, color = '', fill = False):
        self.x = x
        self.y = y
        self.color = color
        self.fill = fill


    def setFillcolor(self, color):
        self.color = color

    def setFilled(self, fill):
        self.fill = fill

    def isFilled(self):
        return self.fill

class Circle(Shape):
    def __init__(self, x = 0, y = 0, color = '', fill = False, radius = 1):
        Shape.__init__(self, x, y, color, fill)
        self.radius = radius

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

        if self.isFilled():
            turtle.fillcolor(self.color)
            turtle.begin_fill()
            turtle.circle(self.radius)
            turtle.end_fill()

        else:
            turtle.circle(self.radius)


class Display:
    def __init__(self, myt=turtle.Turtle(), scr=turtle.Screen()):
        self.turtle = myt
        self.screen = scr
        
        self.screen.delay(0)
        self.turtle.speed(0)
        self.turtle.hideturtle()
        
        self.screen.listen()
        self.screen.onclick(self.mouseEvent)

    def mouseEvent(self, x, y):
        Circle(x, y, randColor(), True, random.randint(10, 100)).draw(self.turtle)


class FlyingTurtle:
    def __init__(self, myt=turtle.Turtle(), scr=turtle.Screen()):
        self.turtle = myt
        self.screen = scr
        self.speed = 6
        self.asteroids = []

        self.screen.delay(0)
        self.turtle.speed(0)
        self.screen.listen()
        self.screen.onkey(self.forward, 'Up')
        self.screen.onkey(self.back, 'Down')
        self.screen.onkey(self.right, 'Right')
        self.screen.onkey(self.left, 'Left')
        self.screen.onclick(self.teleport)
        self.screen.onkey(self.faster, 'x')
        self.screen.onkey(self.slower, 'z')
        self.screen.onkey(self.trail, 'c')


    def forward(self):
        self.turtle.forward(self.speed)

    def back(self):
        self.turtle.forward(-self.speed)
        
    def right(self):
        self.turtle.right(self.speed)

    def left(self):
        self.turtle.left(self.speed)

    def teleport(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()

    def faster(self):
        self.speed += 1

    def slower(self):
        self.speed -= 1

    def trail(self):
        if self.turtle.isdown():
            self.turtle.penup()
        else:
            self.turtle.pendown()

