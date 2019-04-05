# Making a simple dictionary. Stores information about a particular item in a list

alien_0 = {'color': 'green', 'points' : 5} # a dictionary is wrapped in {} braces

print(alien_0['color'])
print(alien_0['points'])
print("\n")

# You can look up how many points an alien is worth by making code like this:
new_points = alien_0['points']

print("You've just earned " + str(new_points) + " points!")
print("\n")

# Adding two new key value pairs
alien_0 = {'color': 'green', 'points' : 5}
print(alien_0)
print('\n')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
