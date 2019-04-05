# sorting a list permanently with the sort() method

cars = ['bmw', 'audi', 'toyota', 'suburu']
cars.sort()
print(cars)
print("\n")

# sorting in reverse alphabetical order..
cars = ['bmw', 'audi', 'toyota', 'suburu']
cars.sort(reverse = True)
print(cars)
print("\n")

# you can sort a list temporarily and maintain the original order of the list using the sorted() method
cars = ['bmw', 'audi', 'toyota', 'suburu']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the list in reverse alphabetical order:")
print(sorted(cars, reverse = True))

print("\nHere is the original list again:")
print(cars)
print("\n")

# printing the list in a reverse order..
cars = ['bmw', 'audi', 'toyota', 'suburu']
print(cars)

cars.reverse() # you can always reverse the order again to go back to the original order
print(cars)
print("\n")

# to find the length of a list use the len() function
cars = ['bmw', 'audi', 'toyota', 'suburu']
print(len(cars))
