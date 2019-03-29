# CSCI 1133, Lab Section 013, lab09 Jeffery Liu, Warm up

def makeDictionary(names, scores):
    newDict = {}
    for n in range(len(names)):
        newDict[names[n]] = scores[n]
    return newDict

def getScore(name, dictionary):
    if name in dictionary:
        return dictionary[name]
    else:
        print('Error: Name not found.')
        return -1
