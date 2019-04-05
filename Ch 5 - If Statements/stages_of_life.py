# Try it yourself, page 89

age = 36

if age < 2:
    print("This person is a baby.\n")
elif age < 4:
    print("This person is a toddler.\n")
elif age < 13:
    print("This person is a kid.\n")
elif age < 20:
    print("This person is a teenager.\n")
elif age < 65:
    print("This person is an adult.\n")
else:
    print("This person is an elder.\n")

age = 12

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print("That person's age makes them a " + str(stage) + ".")
