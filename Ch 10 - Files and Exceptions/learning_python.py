# Try it yourself, page 197

# Reading in the entire file
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
print(contents)
print("\n")

########################################################################

# Looping over the lines
filename = 'learning_python.txt'

with open(filename) as file_object:
   for line in file_object:
        print(line.strip())
print("\n")

###############################################################################

# Storing the lines in a list
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
