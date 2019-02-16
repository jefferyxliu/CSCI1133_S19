# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, A Slice of Pi

#estimate pi function
def estimatePi(sampleSize):
    import random
    import math
    count = 0
    for n in range(0,sampleSize): #throws dart for sample size.
        if math.sqrt((random.uniform(-1,1))**2 + (random.uniform(-1,1))**2) <= 1: #checks if in circle with distance formula
            count += 1 #keeps count
    return count / sampleSize * 4 #returns pi estimate

import math

y_n = 'y'
while y_n == 'y':
    sampleSize = int(input('Input a sample size: ')) #prompts sample size input

    Pi = estimatePi(sampleSize) #estimates pi with function

    #outputs approximation, actual and absolute difference
    print('pi is approximately', Pi)
    print('Actual pi:', math.pi)
    print('Error:', abs(Pi - math.pi))

    y_n = input('Do you wish to continue? (y/n): ')
    print()


