# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, A Slice of Pi


def estimatePi(sampleSize):
    import random
    import math
    count = 0
    for n in range(0,sampleSize):
        if math.sqrt((random.uniform(-1,1))**2 + (random.uniform(-1,1))**2) <= 1:
            count += 1
    return count / sampleSize * 4

import math
y_n = 'y'

while y_n == 'y':
    sampleSize = int(input('Input a sample size: '))
    Pi = estimatePi(sampleSize)
    print('pi is approximately', Pi)
    print('Actual pi:', math.pi)
    print('Error:', abs(Pi - math.pi))
    y_n = input('Do you wish to continue? (y/n): ')
    print()


