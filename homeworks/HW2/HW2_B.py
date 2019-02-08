# CSCI 1133, Lab Section 013, HW 2 Jeffery Liu, Problem B

#fourSidedStar() function with parameter lengthOfSide
def fourSidedStar(lengthOfSide):
    import turtle #using turtle module
    for n in [1,2,3,4]: #exploiting symmetry to iterate the following four times:
        turtle.left(75)
        turtle.forward(lengthOfSide)
        turtle.right(60)
        turtle.forward(lengthOfSide)
        turtle.left(75) #drawing one quadrant of the star.

#main() function
def main():
    lengthOfSide = int(input('Please enter the length of a star\'s sides: ')) #prompting input parameter
    fourSidedStar(lengthOfSide) #executing fourSidedStar() to draw star

#You can use the following to test the function main() out.
#main()
