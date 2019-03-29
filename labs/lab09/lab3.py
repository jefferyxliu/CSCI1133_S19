# CSCI 1133, Lab Section 013, lab09 Jeffery Liu, Counting Keywords

filename = input('Input file name: ')

f = open(filename,'r')

words = f.read().split()

frequencies = {
    'False' : 0,
    'await' : 0,
    'else' : 0,
    'import' : 0,
    'pass' : 0,
    'None' : 0,
    'break' : 0,
    'except' : 0,
    'in' : 0,
    'raise' : 0,
    'True' : 0,
    'class' : 0,
    'finally' : 0,
    'is' : 0,
    'return' : 0,
    'and' : 0,
    'continue' : 0,
    'for' : 0,
    'lambda' : 0,
    'try' : 0,
    'as' : 0,
    'def' : 0,
    'from' : 0,
    'nonlocal' : 0,
    'while' : 0,
    'assert' : 0,
    'del' : 0,
    'global' : 0,
    'not' : 0,
    'with' : 0,
    'async' : 0,
    'elif' : 0,
    'if' : 0,
    'or' : 0,
    'yield' : 0
    }

for x in words:
    if x in frequencies:
        frequencies[x] += 1

print('Keyword frequency in alphabetic order:')

for x in sorted(frequencies):
    if frequencies[x] > 0:
        print('  {0:10}{1}'.format(x, frequencies[x]))
