# CSCI 1133, Lab Section 013, lab11 Jeffery Liu, Measure Class

class Measure:

    def __init__(self, feet = 0, inches = 0):
        totalinches = 12 * feet + inches
        if totalinches >= 0:
            self.feet = totalinches // 12
            self.inches = totalinches % 12

        else:
            self.feet = (totalinches // 12) + 1
            self.inches = (totalinches % 12) - 12

    def __str__(self):
        return '{}\'{}\"'.format(self.feet, self.inches)

    def __add__(self, other):
        return Measure(self.feet + other.feet, self.inches + other.inches)

    def __sub__(self, other):
        return Measure(self.feet - other.feet, self.inches - other.inches)

    

    
