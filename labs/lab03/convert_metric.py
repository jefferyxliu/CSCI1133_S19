# CSCI 1133, Lab Section 013, lab03 Jeffery Liu Metric Conversions

#convert function (only works for specific conversions between first and second half of unitlist)
def convert(value,unit):
    unitlist = ['pounds', 'ounces', 'miles', 'inches', 'kilos', 'grams', 'kilometers', 'centimeters']
    convertvalue = [0.453592,28.3495,1.60934,2.54,2.20462,0.035274,0.621371,0.393701]
    for n in range(0,len(unitlist)):
        if unit == unitlist[n]:
            converted = value * convertvalue[n]
            x = (n + 4) % 8
    return [converted , unitlist[x]]

y_n = 'y'
while y_n == 'y':
    #prompt unit and value
    value = float(input('Enter value: '))
    unit = input('Enter units: ')
    #test for unit in list
    if unit not in ['pounds', 'ounces', 'miles', 'inches', 'kilos', 'grams', 'kilometers', 'centimeters']:
        print(value,unit,'is not a valid unit.')
        raise SystemExit
    #print conversion rounded to 4 decimal places
    print(round(convert(value,unit)[0],4),convert(value,unit)[1])
    #loops to prompt again if input is 'y'
    y_n = input('Do you wish to continue (y/n)? ')
    print()
