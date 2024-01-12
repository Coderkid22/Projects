
IsItAnimal = input('Do you want your character to be an animal, yes or no? ')
keep = 'yesno'
delete = 'abcdefghijklmnopqrstuvwxyz '
IsItAnimal = IsItAnimal.translate(str.maketrans(keep, keep, delete)).lower()
while IsItAnimal.lower() not in ('yes', 'no'):
    print('Invalid input. Enter yes or no ')
    IsItAnimal = input('Do you want your character to be an animal yes or no? ')

if IsItAnimal == 'yes':
    WhatTypeOfAnimal = input('Ok, then what type of animal is it? ')
    BoolAnimal = True
else:
    BoolAnimal = False




gender = input('Is your character a boy or a girl? ')
height = input('What is your characters height in cm? ')
age = input('What is your characters age? ')

CharacterAttributes = (BoolAnimal, gender, height, age, WhatTypeOfAnimal)

if BoolAnimal == True:
    print(f'So your character is a {CharacterAttributes[4]}, is a {CharacterAttributes[1]}, and is {CharacterAttributes[3]} years old.')
else:
    print(f'So your character is a {CharacterAttributes[1]}, is {CharacterAttributes[2]} cm in height, and is {CharacterAttributes[3]} years old.')