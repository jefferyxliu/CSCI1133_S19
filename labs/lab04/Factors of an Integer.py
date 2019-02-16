# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, Factors of an Integer

def factorize(integer):
    factors = []
    n = 2
    while integer > 1:
        if integer % n == 0: #checks if integer is divisible by n
            integer /= n #divides n
            factors.append(n) #adds n to running list of factors
            n -= 1
        n += 1 #checks same factor, or if all n factors have been exhausted, moves to n+1
    return factors

y_n = 'y'
while y_n == 'y':
    factors = factorize(int(input('Input a positive integer: ')))
    print('Factors: ',end = '')

    for n in range(0,len(factors)-1):
        print(factors[n], end = '*')
    print(factors[-1])
    
    y_n = input('Continue (y/n)? ')
    print()
