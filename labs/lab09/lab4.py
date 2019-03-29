# CSCI 1133, Lab Section 013, lab09 Jeffery Liu, Fully Associative Memory Program

def addDB(Dict, a, b):
    if a in Dict:
        if b not in Dict[a]:
            Dict[a].append(b)
    else:
        Dict[a] = [b]
    if b in Dict:
        if a not in Dict[b]:
            Dict[b].append(a)
    else:
        Dict[b] = [a]

def findDB(Dict, a):
    if a in Dict:
        return Dict[a]
    else:
        return []

def removeDB(Dict, a, b):
    if a in Dict:
        if b in Dict[a]:
            Dict[a].remove(b)
        
        if Dict[a] == []:
            del Dict[a]

    if b in Dict:
        if a in Dict[b]:
            Dict[b].remove(a)
        
        if Dict[b] == []:
            del Dict[b]



Dict = {}
commands = ['add','find','del','clear','end','help']
arguments = [' string1 string2',' string',' string1 string2','','',' command']
instruction = [
    'adds the association of \'string1\' with \'string2\' to the database.',
    'displays all associations of \'string\'. Does nothing if \'string\' is not in the database.',
    'removes the association of \'string1\' with \'string2\' from the database. Does nothing if the association of \'string1\' with \'string2\' does not exist.',
    'clears all entries and associations in the database.',
    'exits the program.',
    'gives helpful information about \'command\''
    ]
action = ['']

while action[0] != 'end':
    action = []
    while action == []:
        action = input('>>> ').split()

    if action[0] == 'add':
        if len(action) == 3:
            addDB(Dict, action[1], action[2])
        else:
            print('Error: command \'add\' takes two arguments.')

    elif action[0] == 'find':
        if len(action) == 2:
            print('{}:'.format(action[1]))
            for x in findDB(Dict, action[1]):
                print('  {}'.format(x))
        else:
            print('Error: command \'find\' takes one argument.')  

    elif action[0] == 'del':
        if len(action) == 3:
            removeDB(Dict, action[1], action[2])
        else:
            print('Error: command \'del\' takes two arguments.')

    elif action[0] == 'clear':
        Dict = {}

    elif action[0] == 'help':
        if len(action) != 2:
            print('commands:')
            for x in commands:
                print(' ' + x)
            print('For more info on a command type \'help command\'.')

        elif len(action) == 2:
            for n in range(len(commands)):
                if action[1] == commands[n]:
                    print('\'{}{}\''.format(commands[n], arguments[n]))
                    print('  {}'.format(instruction[n]))
            if action[1] not in commands:
                print('Error: \'{}\' is not a valid command.'.format(action[1]))
            
    elif action[0] not in commands:
        print('Error: \'{}\' is not a valid command.'.format(action[0]))


