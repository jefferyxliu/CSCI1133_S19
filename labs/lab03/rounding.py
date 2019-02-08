# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, Rounding floating-point values

#rounding floating point number
def roundFloat(n):
    if n > 0:
        ni = int(n + 0.5)
    elif n < 0:
        ni = int(n - 0.5)
    elif n == 0:
        ni = 0
    return ni

#prompt a float
x = float(input('Input a floating-point number: '))

#output rounded int
print('The rounded integer is', roundFloat(x))
