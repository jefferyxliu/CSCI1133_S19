t = float(input('Enter temperature in degrees Fahrenheit: '))
v = float(input('Enter wind velocity in miles per hour: '))
windChill = 35.74 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
print('It feels like', windChill, 'degrees Fahrenheit.')
