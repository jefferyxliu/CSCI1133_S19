# CSCI 1133, Lab Section 013, HW 2 Jeffery Liu, Problem C

#calories burned functions, short and tall:
def calories_short(age,weight,heart_rate,time):
    return  ((age * 0.074) + (heart_rate * 0.4472) - (weight * 0.05741) - 20.4022) * time / 4.184

def calories_tall(age,weight,heart_rate,time):
    return  ((age * 0.2017) + (heart_rate * 0.6309) - (weight * 0.09036) - 55.0969) * time / 4.184

def main():
    #prompt parameters
    height = float(input('Please input the height of the person (for example, 5.6 means 5 feet 6 inches): '))
    weight = float(input('Please input the body weight of person, in pounds: '))
    heart_rate = float(input('Please input the average heart rate of the person during the workout, in beats per minute: '))
    age = float(input('Please input the age of the person, in years: '))
    time = float(input('Please input the duration of the workout of the person, in minutes: '))
    #print the entered parameters
    print('')
    print('You entered the following information:')
    print('Height:', height)
    print('Average heart rate:', heart_rate)
    print('Age:', int(age))
    print('Duration of workout:', time)

    #test for tall or short and then print calories burned.
    if height > 5.6:
        print('The number of calories burned for this tall person is', int(calories_tall(age,weight,heart_rate,time)), 'calories.')
    else:
        print('The number of calories burned for this short person is', int(calories_short(age,weight,heart_rate,time)), 'calories.')    

#test:
#main()
