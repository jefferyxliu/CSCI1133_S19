# CSCI 1133, Lab Section 013, lab08 Jeffery Liu, Warm up

def reverseString(x):

    if x == '':         #base case
        return ''

    else:               #recursion
        return x[-1] + reverseString(x[:-1])


# or you can be smart:
# def reverseString(x):
#   return x[::-1]

def maxValue(list1):

    if len(list1) == 1:     #base case
        return list1[0]
    
    elif list1[0] <= list1[1]:          #recursion on list1[1,2,3,4,...]
        return maxValue(list1[1:])
    
    else:                               #recursion on list1[0,2,3,4,...]
        return maxValue([list1[0]]+list1[2:])




    
