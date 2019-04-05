# Try it yourself, page 115

favorite_numbers = {
    'blaine' : [6, 13],
    'sally' : [42, 8 , 12],
    'austin' : [14],
    'phil' : [7, 0],
    'lee' : [9, 108],
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print("\n" + name.title() + "'s favorite numbers are:")
    else:
        print("\n" + name.title() + "'s favorite number is:")

    for number in numbers:
        print("\t" + str(number))
