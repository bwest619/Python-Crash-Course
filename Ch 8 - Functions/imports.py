# Try it yourself, page 159
# Importing from pets_module.py

import pets_module

pets_module.describe_pet('cat', 'gizmo')
print("\n")
##########################################

from pets_module import describe_pet

describe_pet('cat', 'raisin')
print("\n")
############################################

from pets_module import describe_pet as dp

dp('dog', 'boomer')
print("\n")
###############################################

import pets_module as pm

pm.describe_pet('hamster', 'cruizer')
print("\n")
##############################################

from pets_module import *

describe_pet('cat', 'gizmo')
print("\n")

###################################################################################################################

# Importing from album_module for extra practice
from album_module import make_album

make_album() ###### This isn't right. I'll have to come back to this after the next chapter to figure out the right...
            ####### ...way to import this type of function






