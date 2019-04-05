# A module storing a function in a separate file to be recalled in another program
# In other words, a module is a file that contains the code you want to import into your program

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print(topping)

# Going to import this code to the file making_pizzas.py which has to also be in the same directory

