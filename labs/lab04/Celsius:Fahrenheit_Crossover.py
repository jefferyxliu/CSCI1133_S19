# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, Celsius/Fahrenheit Crossover

C = 101
F = 0
while C != F: #Loops until C and F are equal
    C = int(C - 1) #decrements C
    F = int(9 / 5 * C + 32) #calculates F
    #print('Degrees Celsius:', C)
    #print('Degrees Fahrenheit:', F)
    #print()
    
print(C, 'degrees is the same in both Celsius and Fahrenheit.')
