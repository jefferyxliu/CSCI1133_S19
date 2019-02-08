# CSCI 1133, Lab Section 013, HW 2 Jeffery Liu, Problem A

#poiseuille() function with parameters length, radius, viscosity
def poiseuille(length, radius, viscosity):
    import math
    resistance = 8 * viscosity * length / (math.pi * (radius ** 4))
    return resistance

def main():
    #Asking to enter input parameters:
    length = float(input('Please enter the length: '))
    radius = float(input('Please enter the radius: '))
    viscosity = float(input('Please enter the viscosity: '))

    #Testing for non-positive values of input parameters
    if length > 0 and radius > 0 and viscosity > 0:
        print('The resistance is:', poiseuille(length, radius, viscosity)) #prints the resistance
    else:
        print('Failed due to input error. Please make sure your inputs are all positive. Exiting program.') #prints error message
        raise SystemExit #exits the program (even if the function main() is used in another program and more commands follow it.)

#You can use the code below (remove the comment #) to test exiting program.
#main()
#print('This message should not appear if there is an input error, because the program will have exited.')
