# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, Take-Away Game
obj = 21

def nim(obj):
    #optimal choice function
    import random
    if obj % 4 == 0:
        return random.randint(1,3) #no optimal choice if number of objects divisible by four, just choose random
    else:
        return obj % 4    

print('Welcome to the Take-Away Game.')
print('In this game there are a certain number of objects, and players take turns taking away 1, 2, or 3 objects at a time.')
print('The player to take the last object wins.')


if input('Would you like to go first (y/n)?: ') == 'y': #starts turn counter on odd or even depending on who goes first.
    turn = 0
else:
    turn = 1
while obj > 0: #loops until win conditions are met, taking the last object.
    turn +=1 #increments turn counter on each loop

    if turn % 2: #player turn on odd numbers
        choice = 0
        while not choice in range(1,4): #loops if invalid input
            choice = int(input(str(obj) + ' objects remain, choose 1,2 or 3: ')) #prompts player input
            if not choice in range(1,4):
                print('oops, you must choose 1, 2 or 3...')
        obj -= choice #adjusts object number

    else: #computer turn on even numbered turns
        choice = nim(obj) #program uses optimal play function
        print(obj, 'objects remain, I\'ll take', choice)
        obj -= choice #adjusts object number

#determines winner by end turn number, prints winner.    
if turn % 2:
    print('You win!')
else:
    print('I win.')

