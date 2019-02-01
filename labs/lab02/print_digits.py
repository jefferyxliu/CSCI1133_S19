n = int(input('Enter a four digit integer: '))
print(n//1000)
print(n//100-10*(n//1000))
print(n//10-10*(n//100))
print(n-10*(n//10))
    
