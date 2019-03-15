# CSCI 1133, Lab Section 013, lab08 Jeffery Liu, Euclidean GDF

def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if a < b:
        return gcd(b, a)

    if b == 0:
        return a

    else:
        return gcd(b, a % b)

