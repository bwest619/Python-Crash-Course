# Try it yourself, page 131

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    vacation = input("\nIf you could visit one place in the world, where would you go? ")

    responses[name] = vacation

    repeat = input("\nWould you like to let another person respond? (yes/no) \n")
    if repeat == 'no':
        polling_active = False

for name, vacation in responses.items():
    print(name.title() + " wants to visit " + vacation.title() + "!")


