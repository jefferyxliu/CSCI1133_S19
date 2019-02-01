num_ingredients = int(input('Enter number of ingredients: '))

recipe = {}
for m in range(0,num_ingredients):
    o = input('input ingredient ' + str(m+1) + ': ')
    recipe[o] = float(input('ingredient amount (without units): '))
    m = m + 1

recipe_people = int(input('Recipe feeds how many?: '))

num_people = int(input('How many people do you wish to feed?: '))

for l in recipe:
    recipe[l] = recipe[l]*num_people/recipe_people

for p, q in recipe.items():
    print(p, q)

    
