# CSCI 1133, Lab Section 013, lab05 Jeffery Liu, List Construction

word = 'a'
wordlist = []
while word != '':
    word = input('Insert word: ')
    if word != '':
        if word[0].lower() in word[1:].lower():
            wordlist.append(word)

print()
for x in wordlist:
    print(x)
