# CSCI 1133, Lab Section 013, lab11 Jeffery Liu, Vector Class and Particles

import math
import random


class Vector:
    def __init__(self, components = [0, 0, 0]):
        self.components = components[:]

    def __str__(self):
        return str(self.components)

    def getValues(self):
        return self.components

    def setValues(self, components):
        self.components = components[:]

    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.components))

    def __add__(self, other):

        if len(self.components) <= len(other.components):
            return Vector([self.components[n] + other.components[n] for n in range(len(self.components))])
        
        if len(self.components) > len(other.components):
            return Vector([self.components[n] + other.components[n] for n in range(len(other.components))])

    def __sub__(self, other):

        if len(self.components) <= len(other.components):
            return Vector([self.components[n] - other.components[n] for n in range(len(self.components))])
        
        if len(self.components) > len(other.components):
            return Vector([self.components[n] - other.components[n] for n in range(len(other.components))])

    def __mul__(self, scalar):
        return Vector([scalar * x for x in self.components])

    def dot(self, other):
        if len(self.components) <= len(other.components):
            return sum([self.components[n] * other.components[n] for n in range(len(self.components))])
        
        if len(self.components) > len(other.components):
            return sum([self.components[n] * other.components[n] for n in range(len(other.components))])

    def cross(self, other):
        if len(self.components) == 3 and len(other.components) == 3:
            u = self.components
            v = other.components

            return Vector([u[1] * v[2] - u[2] * v[1], - (u[0] * v[2] - u[2] * v[0]), u[0] * v[1] - u[1] * v[0]])




class Particle:

    def __init__(self, mass = 0, position = Vector(), velocity = Vector()):

        self.mass = float(mass)

        self.position = position

        self.velocity = velocity

    def __str__(self):
        return 'mass={}, position={}, velocity={}'.format(self.mass, self.position, self.velocity)


    def setMass(self, m):
        self.mass = m

    def momentum(self):
        return self.velocity * self.mass

    def accelerate(self, a, t):
        self.position = self.position + self.velocity * t + a * (t ** 2 * 0.5)
        self.velocity = self.velocity + a * t



# Simulation
particles = []
for n in range(20):
	particles.append(Particle(0,Vector([random.randint(0,100),random.randint(0,100),0])))

for x in particles:
	print(x)

for x in particles:
	x.accelerate(Vector([0, 0, -9.8]), 10)

for x in particles:
	print(x)


	
