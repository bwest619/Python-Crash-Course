# Try it yourself, page 150

magicians = ['david', 'blaine', 'penn', 'teller']

def show_magicians(magicians):
    """Printing magician names"""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Adding 'the Great!' to the magicians name"""
    # Build a new list to hold the great magicians
    great_magicians = []

    # Make each magician great, and add it to great_magicians
    while magicians:
        magician = magicians.pop()
        great_magician = magician.title() + " the Great!"

        great_magicians.append(great_magician)

    # Add tbe great magicians back into magicians
    for great_magician in great_magicians:
        magicians.append(great_magician)


show_magicians(magicians)   # Prints the original list of magician name
print("\n")

make_great(magicians)   # Calls the function make_great to add to the magician names and re-add to list magicians
show_magicians(magicians)   # Reprints the changed names that were first removed from magicians and then re-added...
                            # ...with changes made
