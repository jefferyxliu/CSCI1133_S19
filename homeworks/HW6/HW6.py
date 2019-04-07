# CSCI 1133, Lab Section 013, HW6 Jeffery Liu

#==========================================
# Problem 1
#==========================================
# Name: sameKeys()
# Purpose: Given two dictionaries, this function returns a third dictionary whose
#   keys are those which the first two have in common, and the corresponding
#   values is a list containing the values for the same key in the first two.
# Constraints: The dictionaries passed in cannot be affected. Preserve order and
#   data structures for the values of the first two when they are returned in
#   combination.
# Input Parameter(s):
#   diction1: a dictionary
#   diction2: a dictionary
# Return Value(s): a dictionary, that combines values of diction1 and diction2
#   that have the same key.
#==========================================

def sameKeys(diction1, diction2):

    # make a new empty dictionary that will be returned at the end.
    diction3 = {}

    # loops through keys of diction1
    for key in diction1:
        # and checks to see if the same is in the keys of diction2
        if key in diction2:
            # if so, concatenates their values as a list, as a value of the same key.
            diction3[key] = [diction1[key], diction2[key]]

    return diction3



#==========================================
# Problem 2
#==========================================
# Name: averageGrades()
# Purpose: Given a dictionary whose values are lists of integers, this function
#   returns a dictionary whose keys are the same, but the value is the average  
#   of the entries in the list that is in the corresponding values of the first
#   dictionary.
# Constraints: The dictionary passed in cannot be affected.
# Precondition: The values in the dictionary passed in will be lists containing
#   integers or an empty list.
# Input Parameter(s):
#   diction: a dictionary, whose values are lists of integers
# Return Value(s): a dictionary, that contains the average of each list in values
#   of diction, under the same key.
#==========================================


def averageGrades(diction):

    # makes a new empty dictionary that will be returned at the end
    diction1 = {}
    
    # loops through keys of diction
    for key in diction:

        if len(diction[key]) > 0:
            # returns the rounded average of the list in the value. (sum divided by length)
            diction1[key] = int(sum(diction[key]) / len(diction[key]))

        else:
            # unless the list is empty, since that would result in divide by 0 error, then 0 is taken as the average. 0
            diction1[key] = 0

    return diction1

#==========================================
# Problem 3
#==========================================
# Name: allKeys()
# Purpose: Given a dictionary whose values are lists and an element, this
#   function returns a sorted list of the keys of the dictionary whose value
#   contains the element.
# Constraints: The dictionary passed in cannot be affected.
# Precondition: The values in the dictionary passed in will be lists containing
#   integers or an empty list. The keys of the dictionary passed in will be strings.
# Input Parameter(s):
#   diction: a dictionary whose keys are strings and values are lists of
#       integers.
#   element: an integer
# Return Value(s): a sorted list of all the keys in diction whose values contain
#       element.
#==========================================

def allKeys(diction, element):

    # make a new empty list to be returned
    keys = []

    # loops keys of diction
    for key in diction:

        # if the elements is in its value
        if element in diction[key]:
            # it is added to the list of keys
            keys.append(key)

    # the sorted list of keys is returned.
    return sorted(keys)

#==========================================
# Problem 4
#==========================================
# Name: invertFiles()
# Purpose: Given a list of names of text files in the same enclosing folder as
#   this program file, this function creates an inverted text file from those
#   text files called 'HW6_output.txt'.
# Constraints: Function will not have user input/output. Files will be read and
#   written in script. The output inverted text file will be sorted ascending
#   order.
# Precondition: The files passed in will be in .txt format. The text files
#   passed in will have the document number as the first line. The rest of the
#   text file will have no contracted words and no numerals and no more than one
#   delimiter in a row.
# Input Parameter(s):
#   list_of_file_names: a list of text file names.
# Return Value(s): None (output is in 'HW6_output.txt')
#==========================================

# importing regular expressions module
import re



def invertFiles(list_of_file_names):

    # creating a new dictionary to store the structure of the inverted text file
    diction = {}

    
    # for each file
    for x in list_of_file_names:

        # open the file in a file object
        f = open(x, 'r')

        # record the document number
        number = f.readline().rstrip('\r\n')

        # store the rest of the text
        text = f.read().lower()

        # split the text using the regular expressions module .split() function.
        data = re.split('[ .,:;!?\s\b]+|[\r\n]+', text)
        # change it to an iterable filter object(?)
        data = filter(None, data)

        # loop through the split text list.
        for word in data:

            # add the word to the dictionary if it not already there, with the
            # document number in as the value.
            if word not in diction:
                diction[word] = [number]

            # or if the word is already in the dictionary and if the document
            # number is not already in the values (i.e. has not appeared in the
            # same document), add its document number to the value list.
            elif number not in diction[word]:
                diction[word].append(number)
                
        # close file
        f.close()
    
    
    # create/open the output file in write mode.
    f1 = open('HW6_output.txt','w')

    # loop through dictionary words in sorted order.
    for word in sorted(diction):

        # loop through document numbers in sorted order.
        for number in sorted(diction[word]):

            # write the word and number to the file.
            f1.write(str(word) + ' ' + str(number) + '\r\n')
            
    # close file
    f1.close()




