# CSCI 1133, Lab Section 013, HW 3 Jeffery Liu, Problem A

#defining function to convert RGB to CMYK
def RGB_to_CMYK(R,G,B):
    K = 1 - max(R,G,B) / 255
    CMYK = []
    if [R,G,B] == [0,0,0]: #since all 0 values results in division by 0, this case is checked separately.
        CMYK = [0,0,0]
    else: #since the formulae are symmetric in RGB, can iterate over [R,G,B] and put the results in order in a new list.
        for x in [R,G,B]: 
            CMYK.append(round((1 - x / 255 - K) / (1 - K) * 100))
    #finally append K to the list and return
    CMYK.append(round(K * 100))
    return CMYK

def main():
    #prompt RGB color inputs
    R = int(input('Red component: '))
    G = int(input('Green component: '))
    B = int(input('Blue component: '))
    #calling RGB_to_CMYK() to convert to CMYK and print the results separated by a space.
    for x in RGB_to_CMYK(R,G,B):
        print(x, end = ' ')
    print() #goes to a new line
