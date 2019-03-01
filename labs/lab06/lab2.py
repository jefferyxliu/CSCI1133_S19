# CSCI 1133, Lab Section 013, lab06 Jeffery Liu, Midterm Preparation

favplaces = ['Venice','Florence','Rome','Naples','Milan']
print(favplaces)
print(sorted(favplaces))
print(sorted(favplaces, reverse = True))
favplaces.reverse()
favplaces.insert(0, 'Genoa')
favplaces.append('Padua')
favplaces.pop()
favplaces.pop(0)
favplaces.pop(0)
print(favplaces[2])
favplaces.remove(favplaces[2])
favplaces[0] = 'TestPlace'
del favplaces[1]
del favplaces[1]
print(favplaces)


person_name = 'Hildegard of Bingen'
person_message = '\tOrdo Virtum is a great song, don\'tcha think?\n'
print(person_name, person_message)
person_message.lstrip()
person_message.rstrip()
person_message.strip()
person_message = person_message.strip()
name_message = person_name + ' says, \"' + person_message + '\"'
print(name_message)

def city_country(city_name, country_name):
    return city_name + ', ' + country_name

def main():
    n = int(input('How many cities would you like to enter?: '))
    cities = []
    countries = []
    for i in range(n):
        cities.append(input('Name of city ' + str(i + 1) + ': '))
        countries.append(input('What country is city ' + str(i + 1) + ' in?: '))

    print()
    for j in range(n):
        print(city_country(cities[j], countries[j]))
    
    k = 0
    while k in range(n):
        print(city_country(cities[k], countries[k]))
        k += 1

magician_names = ['Alakazam','Hypno','Beheeyem', 'Mr. Mime', 'Hoopa', 'Jynx']

def show_magicians(names):
    for x in names:
        print(x)

def make_great(names):
    for n in range(len(names)):
        names[n] = 'Great ' + names[n]

show_magicians(magician_names)
print()
make_great(magician_names)
show_magicians(magician_names)


def my_calculator(list1, list2, operator):
    if operator == '+':
        return [list1[i] + list2[i] for i in range(len(list1))]
    if operator == '-':
        return [list1[i] - list2[i] for i in range(len(list1))]
    if operator == '*':
        return [list1[i] * list2[i] for i in range(len(list1))]
    if operator == '/':
        return [int(list1[i] / list2[i]) for i in range(len(list1))]
    
            
