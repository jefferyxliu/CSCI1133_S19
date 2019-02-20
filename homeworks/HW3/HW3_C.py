# CSCI 1133, Lab Section 013, HW 3 Jeffery Liu, Problem C
print('Welcome to the installment loan evaluation program!')
print()

#prompts inputs, principle, interest and term.
P = float(input('Please input the amount of money you will be borrowing: '))
R = float(input('Please input the interest rate: ')) / 100
T = int(input('Please input the term for the loan (in years): '))

#calculates face value
F = P + (P * R * T)

#checks ranges of inputs
if P > 10000:
    print('Error: The Principle is too high, the maximum is $10000')

if P < 100:
    print('Error: The Principle is too low, the minimum is $100')

if R > 0.15:
    print('Error: The Interest is too high, the maximum is 15%')

if R <= 0:
    print('Error: The Interest is too low, the minimum is 0%')

if T > 10:
    print('Error: The Term is too high, the maximum is 10 years')

if T <= 0:
    print('Error: The Term is too low, the minimum is 0 years')

#prints face value and monthly payment only if in range
if 100 <= P <= 10000 and 0 < R <= 15 and 0 < T <= 10:
    print()
    #print('The face value of the loan is: $' + str(round(F,2)))
    print('The face value of the loan is: $' + str(format(F,'0.2f')))
    print('Your monthly payment each month for', int(T * 12) , 'months is: $' + str(round(F / T / 12,2)))
