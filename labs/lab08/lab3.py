# CSCI 1133, Lab Section 013, lab08 Jeffery Liu, Deep Square 2.0

def flatDeepSquare(list1):

    if all([isinstance(x, int) for x in list1]):
        return [x**2 for x in list1]

    else:
        squarelist = []
        for x in list1:
            if isinstance(x, int):
                squarelist.append(x**2)
            if isinstance(x, list):
                squarelist.extend(flatDeepSquare(x))

    return squarelist
                
