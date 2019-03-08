# CSCI 1133, Lab Section 013, lab07 Jeffery Liu, Letter Frequencies

f = open('shakespeare-julius-26.txt','r')

frequencies = {}

for ch in f.read().lower():
    if ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in frequencies:
            frequencies[ch] = 1
        else:
            frequencies[ch] += 1



for x in sorted(frequencies):
    print('{0}:{1:>5}'.format(x, frequencies[x]))

f.close()
