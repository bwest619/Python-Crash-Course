# Defining a function

# A very simple function that prints a greeting
def greet_user():
    """Display a simple greeting"""
    print("Hello!")


greet_user()
print("\n")

##########################################################################

# Passing information to a function
# By adding username in the parenthesis the function now expects you to provide a value for username each time you call
def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")


greet_user('jesse')

greet_user('sarah')

greet_user('blaine')

# The variable 'username' is a parameter = a piece of information the function needs to do its job.
# The value 'jesse' in greet_user is an argument - a piece of information that is passed from a function call to a function

###############################################################################################

# Using a function with a while loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break


    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
