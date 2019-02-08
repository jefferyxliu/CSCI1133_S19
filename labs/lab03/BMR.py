# CSCI 1133, Lab Section 013, lab03 Jeffery Liu, Basal Metabolic Rate

#prompting inputs
weight = float(input('Please enter your weight in pounds: '))
height = float(input('Please enter your height in inches: '))
age = float(input('Please enter your age in years: '))
gender = ''
while gender != 'M' and gender != 'F':
    gender = input('Please enter your gender (\"M\" or \"F\"): ')

#using conditions and calculating BMR
if gender == 'M':
    BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
if gender == 'F':
    BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)

#output chocolate bars
print('You must consume approximately', BMR/230 ,'chocolate bars per day to maintain your weight.' )
