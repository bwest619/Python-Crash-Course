# Try it yourself. page 150


magicians = ['david', 'blaine', 'penn', 'teller']

def show_magicians(magicians):
    """ Printing magicians names"""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """Adding ' the Great!' to the end of the magicians names"""
    great_magicians = []

    while magicians:
        current_magician = magicians.pop()
        great_magician = current_magician.title() + " the Great!"

        great_magicians.append(great_magician)

    for magician in great_magicians:
        magicians.append(magician)

    return magicians # When you call a function that returns a value, you need to provide a variable for the value...
                        # ...to be stored

show_magicians(magicians)
print("\n")

great_magicians = make_great(magicians[:]) # The variable created to store the returned value
show_magicians(great_magicians)
print("\n")

show_magicians(magicians)
