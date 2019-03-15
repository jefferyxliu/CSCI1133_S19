# CSCI 1133, Lab Section 013, lab08 Jeffery Liu, Super Digit

def superDigit(n):
    if len(str(n)) == 1:
        return n
    else:
        #sum([n//(10**i) % 10 for i in range(len(str(n)))])
        return superDigit(sum([n//(10**i) % 10 for i in range(len(str(n)))]))
