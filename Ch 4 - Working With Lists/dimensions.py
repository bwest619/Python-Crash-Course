# Tuples: Python refers to values that cannot change as immutable, and immutable items are Tuples.
# Sometimes you'll want to create a list of items that cannot change. Tuples allow you to do just that.
# To make a list using tuples you use parenthesis instead of square brackets.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1]) # If I tried to change the value in this dimension by stating dimension[1] = 150, Python will give me an error stating it cannot be done. Hence the parenthesis for the tuple
print("\n")

# You can loop over all the values in a tuple using a for loop as well
for dimension in dimensions:
    print(dimension)
print("\n")

# You can't modify a tuple, but you can assign a new value to a variable that holds a tuple.
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
print("\n")

# Tuples are simple data structures. Use them when you want to store a set of values that should not ve changed throughout the life of a program.