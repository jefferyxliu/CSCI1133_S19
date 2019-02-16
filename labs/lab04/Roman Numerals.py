# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, Roman Numerals

def romannum(integer):
    num = ''
    while integer > 0:
        if integer >= 1000:
            num += 'M'
            integer -= 1000
            
        elif integer >= 900:
            num += 'CM'
            integer -= 900
            
        elif integer >= 500:
            num += 'D'
            integer -= 500
        
        elif integer >= 400:
            num += 'CD'
            integer -= 400
            
        elif integer >= 100:
            num += 'C'
            integer -= 100

        elif integer >= 90:
            num += 'XC'
            integer -= 90

        elif integer >= 50:
            num += 'L'
            integer -= 50

        elif integer >= 40:
            num += 'XL'
            integer -= 40

        elif integer >= 10:
            num += 'X'
            integer -= 10

        elif integer == 9:
            num += 'IX'
            integer -= 9

        elif integer >= 5:
            num += 'V'
            integer -= 5

        elif integer == 4:
            num += 'IV'
            integer -= 4

        else:
            num += 'I'
            integer -= 1

    return num

integer = 0
n = 0
while not integer in range(1,999):
    integer = int(input('Enter and integer value from 1 to 999: '))
    if not integer in range(1,999):
        print('Invalid input.')
        n +=1
    if n == 4:
        raise SystemExit
print('Roman numeral equivalent:', romannum(integer))
        
