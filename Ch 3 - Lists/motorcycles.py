# Changing, adding, and removing elements in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change the first item in the list
motorcycles[0] = "ducati"
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')
print("\n")
print(motorcycles)

# can append items in to an empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print("\n")
print(motorcycles)

# you can add new elements at any position in your list by using the insert() method
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print("\n")
print(motorcycles)

# If you know the position of the item you want to remove from a list, you can use the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']

print("\n")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

print("\n")
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# removing an item using the pop method allows you to use the value of an item after you remove it from the list
# without specifying a location using the pop method, it will automatically pop the last item in the list
motorcycles = ['honda', 'yamaha', 'suzuki']

print("\n")
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print("\n")
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
message = "The last motorcycle I owned was a " + last_owned.title() + "."
print(message)

# you can use pop to remove an item in a list at any position by including the index of the item
print("\n")
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# removing an item by value... removing the value "ducati" from the list
print("\n")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print("\n")
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

