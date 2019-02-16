# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, Take-Away Game
obj = 21

def nim(obj):
    #optimal choice
    import random
    if obj % 4 == 0:
        return random.randint(1,3)
    else:
        return obj % 4    

if input('Would you like to go first (y/n)?: ') == 'y':
    turn = 0
else:
    turn = 1
while obj >= 0:
    turn +=1 #increments turn counter on each loop

    if turn % 2: #player turn on odd numbers
        choice = 0
        while not (1 <= choice <= 3):
            choice = int(input(str(obj) + ' objects remain, choose 1,2 or 3: '))
            if not (1 <= choice <= 3):
                print('oops, you must choose 1, 2 or 3...')
        obj -= choice

    else: #computer turn on even numbered turns
        choice = nim(obj)
        print(obj, 'objects remain, I\'ll take', choice)
        obj -= choice
    
if turn % 2:
    print('You win!')
else:
    print('I win.')

