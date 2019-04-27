import random
import turtle
import math
import time


class Shape:
    def __init__(self, x = [0, 0], color = '', fill = False):
        self.x = x[:]
        self.color = color
        self.fill = fill


    def setFillcolor(self, color):
        self.color = color

    def setFilled(self, fill):
        self.fill = fill

    def isFilled(self):
        return self.fill

class Circle(Shape):
    def __init__(self, x = [0, 0], color = '', fill = False, radius = 1):
        Shape.__init__(self, x, color, fill)
        self.radius = radius

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.x[0],self.x[1])
        turtle.pendown()

        if self.isFilled():
            turtle.fillcolor(self.color)
            turtle.begin_fill()
            turtle.circle(self.radius)
            turtle.end_fill()

        else:
            turtle.circle(self.radius)

class Asteroid(Circle):
    def __init__(self, x = [0, 0], v = [0, 0], radius = 1):
        Circle.__init__(self, x, 'grey', True, radius)
        self.v = v[:]
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()

    def timestep(self):
        for i in range(len(self.x)):
            self.x[i] += self.v[i]

    def draw(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(self.x[0], self.x[1] - self.radius)
        self.turtle.pendown()
        
        self.turtle.fillcolor(self.color)
        self.turtle.begin_fill()
        self.turtle.circle(self.radius)
        self.turtle.end_fill()

    def distance(self, other):
        return (sum((self.x[i]-other.x[i]) ** 2 for i in range(len(self.x)))) ** 0.5

    def collision(self, other):
        return self.distance(other) < self.radius
 
class SpaceShip(Shape):
    def __init__(self, x = [0, 0], v = [0, 90], color = 'red'):
        self.x = x[:]
        self.v = v[:]
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.color = color
        self.radius = 0

    def draw(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(self.x[0], self.x[1])
        self.turtle.pendown()
        self.turtle.left(self.v[1])

        self.turtle.fillcolor(self.color)
        self.turtle.begin_fill()
        self.turtle.right(180-15)
        self.turtle.forward(20)
        self.turtle.right(15+90)
        self.turtle.forward(40*math.sin(math.pi/12))
        self.turtle.right(90+15)
        self.turtle.forward(20)
        self.turtle.left(15)
        self.turtle.end_fill()

        self.turtle.right(self.v[1])

    def timestep(self):
        for i in range(len(self.x)):
            self.x[i] += self.v[0]*[math.cos, math.sin][i](self.v[1]*math.pi/180)

class Game:
    def __init__(self, shipcolor = 'red'):

        self.asteroids = []
        self.ship = SpaceShip([0, 0], [0, 90], shipcolor)
        self.screen = turtle.Screen()
        self.screen.bgpic('space.gif')
        self.screen.screensize(500, 500)
        self.screen.tracer(0)
        self.start = time.time()
        self.generate_asteroid()
        self.generate_asteroid()
        self.generate_asteroid()

        live = True
        while live:
            
            self.screen.listen()
            self.screen.onkey(self.accel, 'Up')
            self.screen.onkey(self.decel, 'Down')
            self.screen.onkey(self.right, 'Right')
            self.screen.onkey(self.left, 'Left')
            self.screen.onkey(self.generate_asteroid, 'x')
            self.timestep()
            if self.collision():
                live = False

        self.end = time.time()

    def timestep(self):

            for x in self.asteroids:
                x.timestep()
                for i in range(len(x.x)):
                    x.x[i] %= 500
                    if x.x[i] > 250:
                        x.x[i] -= 500
                x.draw()

            self.ship.timestep()
            for i in range(len(self.ship.x)):
                self.ship.x[i] %= 500
                if self.ship.x[i] > 250:
                    self.ship.x[i] -= 500
            self.ship.draw()
            self.screen.update()
        
    def generate_asteroid(self):
        distance = 0
        while distance < 100:
            x = Asteroid([random.randint(-250, 250), random.randint(-250, 250)],[random.randint(-3, 3), random.randint(-3, 3)], random.randint(10,50))
            distance = x.distance(self.ship)
        self.asteroids.append(x)

    def accel(self):
        self.ship.v[0] += 1

    def decel(self):
        self.ship.v[0] -= 1

    def right(self):
        self.ship.v[1] -= 10

    def left(self):
        self.ship.v[1] += 10

    def collision(self):
        for x in self.asteroids:
            if x.collision(self.ship):
                return True




print('                     ASTEROIDS')
print('====================================================')
print('                 Press << Enter >>')
input()
print('====================================================')
print('                    Instructions')
print(' Use the arrow keys to maneuver your spaceship and')
print('   avoid collision with the asteroids.')
print(' Press \'x\' to generate more asteroids for a higher')
print('   score multiplier.')
print(' Survive as long as you can!')
print('====================================================')
print('             Press << Enter >> to Continue')
input()
print('====================================================')
print(' Select a ship color:')
print('   1. red')
print('   2. orange')
print('   3. yellow')
print('   4. green')
print('   5. blue')
print('   6. purple')
print('<< Type a number 1-6 >>')
choice = input('>>> ')
if choice.isnumeric():
    color = ['red','orange','yellow','green','blue','purple'][(int(choice) - 1) % 6]
else:
    color = choice
print('====================================================')
print('                       Ready?')
print()
print('             Press << Enter >> to Start')
input()
c = Game(color)
print('====================================================')
print('                   You Crashed!')
print()
print('            Number of Asteroids: {0:>4}'.format(len(c.asteroids)))
print('            Time Survived:       {0:>4}'.format(int(c.end-c.start)))
print('            Score:               {0:>4}'.format(len(c.asteroids)*int(c.end-c.start)))
print('====================================================')
