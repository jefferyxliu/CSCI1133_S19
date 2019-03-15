# CSCI 1133, Lab Section 013, lab08 Jeffery Liu, Deep Square

def deepSquare(list1):

    for n in range(len(list1)):

        if isinstance(list1[n],int):
            list1[n] **= 2
        elif isinstance(list1[n],list):
            deepSquare(list1[n])

        return list1
