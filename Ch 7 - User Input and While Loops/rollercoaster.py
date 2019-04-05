# Using int() to accept numerical input

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!\n")
else:
    print("\nYou'll be able to ride when you're a little older.\n")

#####################################################

age = input("How old are you? ")
age = int(age)

if age >= 21:
    print("You can have a drink here.\n")
else:
    print("You must be at least 21 years old to have an alcoholic beverage here.\n")
