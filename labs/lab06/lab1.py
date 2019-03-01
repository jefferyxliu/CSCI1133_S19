# CSCI 1133, Lab Section 013, lab06 Jeffery Liu, Shortest Distance

import math
def computeArea(x):
    return 3.1415926535898 * x ** 2

radius = float(input("enter a radius: "))
print("The area of a circle with radius ", radius, "is: ", computeArea(radius))


#==========================================
# Name: Dist()
# Purpose: Given two points in the form of a position row vectors [x, y, ...],
#   returns the magnitude of the difference between the two points (i.e the distance).
# Precondition: 
# Input Parameter(s)
#   a, b two coordinate points in the form [x, y, ...].
# Return Value(s)
#   a float value of |a - b|, the distance between a and b
#============================================

def Dist(a, b):
    if len(a) > len(b):
        b.extend([0] * (len(a) - len(b)))
    if len(b) > len(a):
        a.extend([0] * (len(b) - len(a)))

    cpnts = 0
    for n in range(len(a)):
        cpnts += (a[n] - b[n]) ** 2

    return math.sqrt(cpnts)


#==========================================
# Name: shortestDist()
# Purpose: Given a list of points, return the shortest distance between any two points.
# Precondition: The list will only contain pairs of numbers.
# Input Parameter(s)
#   coordlist: a list containing coordinate points in the form [x,y].
# Return Value(s)
#   a float value of the shortest distance between any two points in coordlist
#============================================

def shortestDist(coordlist):
    distlist = []

    for n in range(len(coordlist)):
        for m in range(n + 1, len(coordlist)):
            distlist.append(Dist(coordlist[n], coordlist[m]))

    return min(distlist)


coordlist = [[45, -99], [24, 83], [-48, -68], [-97, 99], \
[-8, -77], [-2, 50], [44, 41], [-48, -58], \
[-1, 53], [14, 86], [31, 94], [12, -91], \
[33, 50], [82, 72], [83, -90], [10, 78], \
[7, -22], [90, -88], [-21, 5], [6, 23]]

print('The shortest distance in the provided list is', shortestDist(coordlist))
