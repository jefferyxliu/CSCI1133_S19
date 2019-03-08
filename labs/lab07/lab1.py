# CSCI 1133, Lab Section 013, lab07 Jeffery Liu, Generating Synthetic Test Data
import random

filename = input('Input file name: ')

f = open(filename,'w')


for i in range(1000):
    f.write(str(i) + ',' + str(random.randint(-1000,1000)) + '\n')

f.close()

f = open(filename,'r')

for line in f:
    print(line, end = '')

f.close()
