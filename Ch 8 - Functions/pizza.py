# Passing an arbitrary number of arguments
# Sometimes you won't know ahead of time how many arguments a function needs to accept
# Python allows a function to collect an arbitrary number of arguments from the calling statement
# Here's a function that builds a pizza when you don't know how many toppings will be needed for the pizza

def make_pizza(*toppings): # The asterisk tells Python to make an empty tuple called toppings
    """Print the list of toppings that have been requested"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

###############################################################################################

# Replace the print statement with a loop that runs through the list of toppings and describes the pizza

def make_pizza(*toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

###########################################################################################

# Mixing positional and arbitrary arguments
# If a function accepts several different kinds of arguments, the parameter for arbitray numbers must come last

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")

    for topping in toppings:
        print(topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
