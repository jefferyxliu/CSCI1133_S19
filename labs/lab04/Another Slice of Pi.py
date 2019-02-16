# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, Another Slice of Pi

def estimatePi2(tolerance):
    import math
    estimate = 1
    n = 0
    while tolerance < 6 / math.sqrt(3) / 3**n / (2 * n + 1):
        n += 1
        partialsum = 0
        for m in range(0,n):
            partialsum += (-1)**m / 3**m / (2 * m + 1)
        estimate = partialsum * 6 / math.sqrt(3)
    return (estimate, n)

tolerance = float(input('input tolerance: '))
x = estimatePi2(tolerance)
print('estimate:', x[0])
print('number of terms:', x[1])
