# CSCI 1133, Lab Section 013, lab10 Jeffery Liu, Polynomials - Again!

import numbers

class Poly:

    def __init__(self, constant = 0, *args):
        if isinstance(constant, numbers.Number):
            n = len(args) - 1
            if len(args) > 0:
                
                while args[n] == 0 and n > 0:
                    n -= 1
            self.coefficients = [constant] + [x for x in args[:n + 1]]

        elif isinstance(constant, str):
            c = constant.replace(' ','').replace('-','+-').split('+')

            self.coefficients = [0]    
            for x in c:
                if 'x' in x:
                    if x[:index('x')] in ['','-']:
                        x = x.replace('x','1x')
                        
                    if '^' in x:
                        self.coefficients.addTerm(int(x[index('^') + 1:]), float(x[:index('x')]))
                        
                    else:
                        self.coefficients.addTerm(1, float(x[:index('x')]))
                        
                else:
                    self.coefficients.addTerm(0, float(x,0))

        elif isinstance(constant, list):
            n = len(constant) - 1
            while constant[n] == 0 and n > 0:
                n -= 1
            self.coefficients = [x for x in constant[:n + 1]]

    def degree(self):

        return len(self.coefficients) - 1

    def insertTerm(self, exponent, coefficient):

        if exponent > len(self.coefficients) - 1:
            self.coefficients.extend([0] * (exponent - len(self.coefficients) + 1))
        self.coefficients[exponent] = coefficient

    def addTerm(self, exponent, coefficient):
        
        if exponent > len(self.coefficients) - 1:
            self.coefficients.extend([0] * (exponent - len(self.coefficients) + 1))
        self.coefficients[exponent] += coefficient

        

    def __str__(self):
        string = ''
        for n in range(len(self.coefficients) - 1, -1, -1):
            if self.coefficients[n] != 0:
                if self.coefficients[n] < 0:
                    string += ' - '

                elif n < len(self.coefficients) - 1:
                    string += ' + '

            
                if n > 1:
                    if abs(self.coefficients[n]) != 1:
                        string += str(abs(self.coefficients[n])) + 'x^' + str(n)
                    else:
                        string += 'x^' + str(n)
            
                elif n == 1:
                    if abs(self.coefficients[n]) != 1:
                        string += str(abs(self.coefficients[n])) + 'x'
                    else:
                        string += 'x'
                     
                elif n == 0:
                    string += str(abs(self.coefficients[n]))

        if self.coefficients == [0]:
            string = '0'

        return string.lstrip()


    def __add__(self, other):
        x = self.coefficients[:]
        y = other.coefficients[:]

        if len(x) < len(y):
            x.extend([0] * (len(y) - len(x)))
        if len(x) > len(y):
            y.extend([0] * (len(x) - len(y)))

        return Poly([x[n] + y[n] for n in range(len(x))])

    def __sub__(self, other):
        x = self.coefficients[:]
        y = other.coefficients[:]

        if len(x) < len(y):
            x.extend([0] * (len(y) - len(x)))
        if len(x) > len(y):
            y.extend([0] * (len(x) - len(y)))

        return Poly([x[n] - y[n] for n in range(len(x))])

    def __mul__(self, other):
        x = self.coefficients[:]
        y = other.coefficients[:]
        z = Poly()
        for i in range(len(x)):
            for j in range(len(y)):
                z.addTerm(i + j, x[i] * y[j])
        return Poly(z.coefficients)

    def differentiate(self):
        self.coefficients = [self.coefficients[n] * n for n in range(1,len(self.coefficients))]

    def integrate(self):
        self.coefficients = [0] + [self.coefficients[n] / (n + 1) for n in range(len(self.coefficients))]
            
    
    def evaluate(self, x):
        return sum([self.coefficients[n] * x**n for n in range(len(self.coefficients))])
