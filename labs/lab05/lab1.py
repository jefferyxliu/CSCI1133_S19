# CSCI 1133, Lab Section 013, lab05 Jeffery Liu, Histograms

import random

histogram = [0] * 13

for n in range(10000):
    histogram[random.randint(1,6) + random.randint(1,6)] += 1

for n in range(2,13):
    print(format(n,'2d') + ':' + format(histogram[n],'5d'))

