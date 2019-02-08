# CSCI 1133, Lab Section 013, lab03 Jeffery Liu Day of the Week

#day of week function according to Zeller's congruence
def dayofweek(m,d,y):
    if m == 1 or m == 2:
        m += 12
        y -= 1
    return (d + 5 + ((26 * (m + 1)) // 10) + ((5 * (y % 100)) // 4) + ((21 * (y // 100)) // 4)) % 7

y_n = 'y'
while y_n == 'y':
    #prompt inputs of month, day, and year
    month = int(input('Enter month: '))
    day = int(input('Enter day: '))
    year = int(input('Enter year: '))
    #uses dayofweek() and finds name of day of week
    weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'][dayofweek(month,day,year)]
    #print day of week
    print(str(month) + '/' + str(day) + '/' + str(year), 'is a', weekday)
    #loops to prompt again if input is 'y'
    y_n = input('Do you wish to continue (y/n)? ')
    print()
    
