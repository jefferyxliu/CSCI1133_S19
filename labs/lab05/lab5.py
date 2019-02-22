# CSCI 1133, Lab Section 013, lab05 Jeffery Liu, English to Pig Latin Translator

def isVowel(a):
    if a.lower() in 'aeiou':
        return True
    else:
        return False

def isCapital(a):
    if a in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        return True
    else:
        return False

def PLword(word):
    if isVowel(word[0]):
        return word + 'way'
    else:
        
        initialconsonant = ''
        n = 0
        while not isVowel(word[n]):
            initialconsonant += word[n]
            n += 1
        if isCapital(word[0]):
            return word[n].upper() + word[n + 1:] + initialconsonant.lower() + 'ay'
        else:
            return word[n:] + initialconsonant + 'ay'

def breakstring(words):
    wordlist = []
    n = 0
    while not words == '':
        if words[n] in ' .,?!:;-+=<>`~@#$%^&*(){}[]|/1234567890\"\'\\':
            wordlist.append(words[:n])
            wordlist.append(words[n])
            if not words == '':
                words = words[n+1:]
            n = -1
        n += 1
    return wordlist
            
def PLstring(words):
    string = ''
    for x in breakstring(words):
        if x in ' .,?!:;-+=<>`~@#$%^&*(){}[]|/1234567890\"\'\\':
            string += x
        else:
            string += PLword(x)
    return string

words = input('Enter a phrase to be translated into Pig Latin: ')
print(PLstring(words))
        
    
