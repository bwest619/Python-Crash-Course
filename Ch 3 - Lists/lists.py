# lists are a collection of items in a particular order

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[0].upper())

print("\n" + bicycles[1])
print(bicycles[3])

#python has a special syntax for accessing the last item in a list. This is done by asking for the item at index -1
print("\n" + bicycles[-1])

#index -2 receives the second item from the end of the list. index -3 receives the third item from the end of the list, and so on
print("\n" + bicycles[-2])
print(bicycles[-3])
print(bicycles[-4])

message = "\nMy first bicycle was a " + bicycles[2].title() + "!"
print(message)
