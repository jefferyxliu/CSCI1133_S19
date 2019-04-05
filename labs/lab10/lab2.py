# CSCI 1133, Lab Section 013, lab10 Jeffery Liu, Sentence Class and Redux

class Sentence:

    def __init__(self, sentence):
        self.sentence = str(sentence)

    def getSentence(self):
        return self.sentence

    def getWords(self):
        return self.sentence.split()

    def getLength(self):
        return len(self.sentence)

    def getNumWords(self):
        return len(self.sentence.split())



class SentenceV1:
    def __init__(self, sentence):
        self.sentence = sentence.split()

    def getSentence(self):
        return ' '.join(self.sentence)

    def getWords(self):
        return self.sentence

    def getLength(self):
        return len(' '.join(self.sentence))

    def getNumWords(self):
        return len(self.sentence)
