# CSCI 1133, Lab Section 013, lab10 Jeffery Liu, Warm up

class Rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den

    def __str__(self):
        if self.numerator % self.denominator == 0:
            return str(int(self.numerator / self.denominator))
        else:
            return str(self.numerator) + '/' + str(self.denominator)

    def scale(self, c):
        self.numerator *= c
        self.denominator *= c

    
