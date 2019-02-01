n = int(input('Enter a positive integer: '))

for m in range(0,len(str(n))):
    print((n//(10**(len(str(n))-m-1)))%10)
