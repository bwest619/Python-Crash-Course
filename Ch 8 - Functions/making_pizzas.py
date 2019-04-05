# Importing an entire module to your program
# Importing the code from the file pizza_module.py

import pizza_module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")

##################################################################################################################

# You can also import a specific function from a model like so:
            # from module_name import function_name

# You can import as many functions as you want from a module by separating each function's name with a comma:
            # from module_name import function_0, function_1, function_2

# Previous example would look like this if all we wanted was to import just the function we're going to use:
            # from pizza_module import make_pizza
from pizza_module import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")
# In the example above you don't need to use the dot notation when you call a function using this syntax...
# ...because we've explicitly imported the function make_pizza() in the import statement.

######################################################################################################################

# If the name of a function you're importing might conflict with an existing name in your program....
# ...you can use a short, unique alias = an alternate name similar to a nickname for the function

# Giving the function make_pizza() an alias, mp(), by importing make_pizza as mp
from pizza_module import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")

#######################################################################################################################

# You can also provide an alias for your module name
# Giving the alias p for pizza_module can make calling your function by just p.make_pizza() is much easier
import pizza_module as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")
# By renaming your module like this helps redirect your attention from the module name and allows you to focus on the ..
# ..descriptive names of its functions

###################################################################################################################

# You can tell Python to import every function in a module by using the asterisk (*) operator

from pizza_module import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
