# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, Another Slice of Pi

#defines function
def estimatePi2(tolerance):
    import math
    estimate = 1
    n = 0
    while tolerance < 6 / math.sqrt(3) / 3**n / (2 * n + 1): #until n-th term of sequence (= difference of partial sums of n and n-1) is less than tolerance:
        n += 1
        partialsum = 0
        #computes partial sums
        for m in range(0,n):
            partialsum += (-1)**m / 3**m / (2 * m + 1)
        estimate = partialsum * 6 / math.sqrt(3)
    return (estimate, n) #returns estimate and terms

#prompts tolerance
tolerance = float(input('input tolerance: '))
x = estimatePi2(tolerance)

#prints esimate and terms
print('estimate:', x[0])
print('number of terms:', x[1])
