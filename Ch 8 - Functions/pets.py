# Passing arguments... a function call may need multiple arguments as a function definition can have multiple parameters
# Positional arguments - need to be in the same order the parameters were written
# Keyword arguments - a name-value pair that you pass to a function

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')


############################################################################

# You can call a function as many times as needed. Here's doing the same program a second time
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('cat', 'gizmo')


###########################################################################

# Using keyword arguments. Directly associate the name and the value within the argument...
# ...This is done so there is no confusion when you pass the argument to the function

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')  # Now we won't accidentally have 'hamster' as pets name
# By using keyword, we can write this as.. describe_pet(pet_name = 'harry', animal_type = 'hamster') as well

###################################################################################################################

# Default values for each parameter
print("\n")


def describe_pet(pet_name, animal_type='dog'):  # When you use default values, any parameter with a default value needs
    # ...to be listed after all the parameters that don't have default values.
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('harry')

#########################################################################################################

print("\n")


def describe_pet(animal_type='dog', pet_name='harry'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet()

###################################################################################################

print("\n")


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('harry', 'hamster')  # Even though animal_type = 'dog', by placing 'hamster' down here it changes the...
# ...value of animal_type to 'hamster'
