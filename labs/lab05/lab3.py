# CSCI 1133, Lab Section 013, lab05 Jeffery Liu, Find the Smallest Number

def minimumIndex(mylist,index):
    minimum = mylist[index]
    for n in range(index,len(mylist)):
        if  minimum > mylist[n]:
            minimum = mylist[n]
    return mylist[index:].index(minimum) + index
