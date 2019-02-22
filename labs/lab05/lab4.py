# CSCI 1133, Lab Section 013, lab05 Jeffery Liu, Exponent Function x ^ y

def mult(a,b):
    multiple = 0
    for n in range(b):
        multiple += a
    return multiple

    

def expo(x,y):
    exponent = 1
    for m in range(y):
        multiple = 0 # this part is the same as mult(exponent,x)
        for n in range(x): #
            multiple += exponent #
        exponent = multiple #this the same as exponent = mult(exponent,x)
    return exponent
