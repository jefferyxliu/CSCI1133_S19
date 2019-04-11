# CSCI 1133, Lab Section 013, HW5 Jeffery Liu

#==========================================
# Problem 1
#==========================================
# Name: cnt_occur()
# Purpose: Given a list of integers and/or strings (which may be embedded)
#   and a value that is an integer or string, this function returns the number
#   of occurences of the value in the list.
# Constraints: The function must use recursion, and may not use other looping
#   constructs. The list passed in cannot be affected.
# Precondition: Only integers and strings will be in the list, only integers and
#   strings can be counted for occurences.
# Input Parameter(s):
#   list1: a list, which may be embedded, containing integers and strings
#   value: an integer or string to be counted
# Return Value(s): an integer, the number of occurences of value in list1
#==========================================

def cnt_occur(list1, value):

    # base case: an empty list has zero occurences.
    if list1 == []:
        return 0

    # looking at the zeroth position:

    # if it is an embedded list, count occurences in embedded list and in the rest of the outer list.
    elif isinstance(list1[0],list):
        return cnt_occur(list1[0], value) + cnt_occur(list1[1:], value)

    # if it is the value, add 1 and count the rest of list.
    elif list1[0] == value:
        return 1 + cnt_occur(list1[1:], value)

    # if it is not the value, just count the rest of the list.
    else:
        return cnt_occur(list1[1:], value)

#==========================================
# Problem 2
#==========================================
# Name: position()
# Purpose: Given a list of integers and/or strings and a value that is an
#   integer or string, this function returns the positions of all occurences
#   of the value in the list. If the value does not occur, an empty list is
#   returned.
# Constraints: The function must use recursion, and may not use other looping
#   constructs. The list passed in cannot be affected.
# Precondition: Only integers and strings will be in the list, only the
#   position of integer or string value can be found.
# Input Parameter(s):
#   list1: a list containing integers and strings
#   element: an integer or string
# Return Value(s): a list, containing the integer positions of each occurence
#   of element in list1
#==========================================
# Name: helper()
# Purpose: Actually contains all the code for positon, except it uses an extra
#   argument to keep track of position. position() calls this function.
# Constraints: same as position()
# Precondition: same as position()
# Input Parameter(s):
#   list1: a list containing integers and strings
#   element: an integer or string
#   n: an integer to keep track of the position.
# Return Value(s): a list, containing the integer positions of each occurence
#   of element in list1
#==========================================



def helper(list1, element, n = 0):

    # base case: an empty list has no occurences of the element.
    if n == len(list1):
        return []

    # looking at the fist position:

    # if it is the element, concatenate its position with the list of positions
    # after it.
    elif list1[n] == element:
        return [n] + position(list1, element, n + 1)

    # if it is not the element, just move on the the rest of the list.
    else:
        return position(list1, element, n + 1)


def position(list1, element):
    return helper(list1, element)


#==========================================
# Problem 3
#==========================================
# Name: rm_conseq_dups()
# Purpose: Given a list of integers and/or strings, this function returns a new
#   list in which all consecutive duplicate elements are removed.
# Constraints: The function must use recursion, and may not use other looping
#   constructs. The list passed in cannot be affected.
# Precondition: Only integers and strings will be in the list, only integers and
#   strings can be counted for occurences.
# Input Parameter(s):
#   list1: a list containing integers and strings
# Return Value(s): a new list, which is list1 with consecutive duplicate
#   elements removed
#==========================================

def rm_conseq_dups(list1):

    # base case1: an empty list has no duplicates.
    if list1 == []:
        return []

    # base case2: a list of length 1 also has no duplicates.
    elif len(list1) == 1:
        return [list1[0]]

    # looking in the zeroth and first position:

    # if they are the same, slice off the first value and move on the rest of the list.
    elif list1[0] == list1[1]:
        return rm_conseq_dups(list1[1:])

    # if they are different, concatenate the zeroth position with the rest of the list in duplicates removed.
    else:
        return [list1[0]] + rm_conseq_dups(list1[1:])


#==========================================
# Problem 4
#==========================================
# Name: sequence()
# Purpose: Given an integer index, this function returns the corresponding value
#   in the sequence {3, 6, 12, 24, 48, ...}, where the first value is 3 and each
#   subsequent value is 2 times the previous.
# Constraints: The function must use recursion, and may not use other looping
#   constructs.
# Precondition: The index must be an integer that is greater than 0.
# Input Parameter(s):
#   n: an integer > 0, the index for the sequences
# Return Value(s): the integer value in the sequence {3*2^(n-1)} with index n.
#==========================================

def sequence(n):
    # base case: the first value of the sequence is 3.
    if n == 1:
        return 3
    
    # every other value is two times the previous value.
    elif n > 1:
        return 2 * sequence(n - 1)


#==========================================
# Problem 5
#==========================================
# Name: rangeIt()
# Purpose: Given an integer starting value and an integer stoping value, this
#   function returns a list of all the integers between the start and stop,
#   (including the start and stop).
# Constraints: The function must use recursion, and may not use other looping
#   constructs.
# Precondition: the start and stop values must be integers, and the start value
#   must be less than or equal to the stop value.
# Input Parameter(s):
#   start: an integer
#   stop: an integer
# Return Value(s): a list, that contains the range of integers between and
#   including the start and stop values.
#==========================================

def rangeIt(start, stop):

    # base case: if the start and stop value are the same, return a list with just the value.
    if start == stop:
        return [start]

    # if the start value is less than the stop, concatenate the start value with the range with start value one higher.
    elif start < stop:
        return [start] + rangeIt(start + 1, stop)
