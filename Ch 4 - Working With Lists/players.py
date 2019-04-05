# working with part of a list... known as a 'slice'. This is slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli'] # prints the first three items in the list
print(players[0:3])
print("\n")

players = ['charles', 'martina', 'michael', 'florence', 'eli'] # printing the second, third, and fourth items in a list
print(players[1:4])
print("\n")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) # omitting the first index in a slice will automatically start your slice at the very beginning
print("\n")         # this will print the first four items of your list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) # omitting the last index in a slice will automatically print to the very end of the list
print("\n")        # this prints from the third item in the list through the very last item in the list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:]) # if we want to print the last three items in a list we can use negative numbers
print("\n")         # prints the last three players and would continue to work as the list of players changes in size

# looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
print("\n")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here is a list of the last four players on my team:")
for player in players[1:]:
    print(player.title())
    



