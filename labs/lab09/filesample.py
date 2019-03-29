# CSCI 1133, Lab Section 013, HW4 Jeffery Liu

#==========================================
# Problem 1
# Name: separate_int_and_str()
# Purpose: Given a list of integer and strings, create two new lists. One
#   list will contain the integers and the other list will contain the
#   strings.
# Precondition: The list will only contain ints and strings
# Input Parameter(s)
#   mylist: a list containing integers and strings
# Return Value(s)
#   -- if the input parameter is an empty list , return a list
#       with two empty lists: [ [ ], [ ] ]
#   -- else return a list with the 0th index position containing the
#       list of integers, and the 1st index position containing the
#       list of strings. If there are no ints or strings, return
#       an empty list in that position
#============================================

def separate_int_and_str(mylist):

    integerlist = []                    # initialize empty int and str lists
    stringlist = []

    for x in mylist:                    # iterates through mylist
        if isinstance(x, int):          # depending on the type of the entry
            integerlist.append(x)       # appends the value to the corresponding list
        if isinstance(x, str):
            stringlist.append(x)

    return [integerlist, stringlist]    # returns both integer and string lists in a list



#==========================================
# Problem 2
# Name: average_of_lists()
# Purpose: Given a list of sublists of integers, create a new list that
#   contains the averages of each sublist.
# Precondition: The list will only contain numbers
# Input Parameter(s)
#   mylist: a list of lists containing numbers
# Return Value(s)
#   a list for which each entry is the average of the values of the sublist
#   in mylist with the corresponding index
#============================================

def average_of_lists(mylist):
    averagelist = []                                # initializes empty list

    for x in mylist:                                # for each sublist
        averagelist.append(round(sum(x) / len(x)))  # appends the rounded average
                                                    #   to initial list
                                                    #   (average = sum / length)

    return averagelist                              # returns list of averages



#==========================================
# Problem 3
# Name: min_of_lists()
# Purpose: Given a list of sublists of integers, return the minimum value
#   over all of the sublists
# Precondition: The list will only contain numbers
# Input Parameter(s)
#   mylist: a list of lists containing numbers
# Return Value(s)
#   a minimum value (a number) of over all of the sublists
# Constraint(s)
#   may not use built in minimum functions
#============================================

def min_of_lists(mylist):

    if len(mylist) == 0:            # if argument is empty list with length 0
        return 0                    # returns 0

    else:
        minimum = mylist[0][0]      # initialize a minimum value as the first entry of first list

        for sublist in mylist:      # iterates through mylist
            for x in sublist:       # iterates through sublist of mylist

                if x < minimum:     # if there is a smaller value
                    minimum = x     # it becomes the new minimum

    return minimum                  # returns the minimum value


#==========================================
# Problem 4
# Name: greater_than()
# Purpose: Given a list of numbers and a number, test if every value on the list is
#   greater than the number
# Precondition: The list will only contain numbers
# Input Parameter(s)
#   mylist: a list of numbers
#   x: a number
# Return Value(s)
#   -- if every element in mylist is greater than x, return True
#   -- else return False    
# Constraint(s)
#   may not use built in functions
#============================================

def greater_than(mylist, x):

    for value in mylist:        # iterates through mylist
        if x >= value:          # if any value is <= x
            return False        # test fails and returns False

    else:                       # otherwise, all values are greater
        return True             # and returns True



#==========================================
# Problem 5
# Name: selection_sort()
# Purpose: Given a list of numbers, sort them in place from smallest to largest
#   with the selection sort algorithm
# Precondition: The list will only contain numbers
# Input Parameter(s)
#   mylist: a list of numbers
# Actions(s)
#   sorts mylist with the selection sort algorithm
# Return Value(s)
#   None
# Constraint(s)
#   may not use built in sorting, minimum or index finding functions.
#============================================

def selection_sort(mylist):

    for n in range(len(mylist)):                    # iterates through each index of mylist

        minimum_index = n                           # each time initializes a minimum index

        for m in range(n, len(mylist)):             # for the entries after the index,

            if mylist[m] < mylist[minimum_index]:
                minimum_index = m                   # if it is smaller, its index becomes
                                                    #   the new minimum index

        placeholder = mylist[minimum_index]         # swaps the entry of index with
        mylist[minimum_index] = mylist[n]           #   the minimum value
        mylist[n] = placeholder

    return                                              # returns None
