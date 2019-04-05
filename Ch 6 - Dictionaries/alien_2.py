# Starting with an empty dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print('\n')

# Modifying values in a dictionary
alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'color' : 'yellow'}
print("The alien's color is now " + alien_0['color'] + ".")
print('\n')





# Modifying values even more
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print("Original x_position: " + str(alien_0['x_position']))
print('\n')

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))





# Removing key-value pairs from a dictionary
alien_0 = {'color' : 'green', 'points': 5}
print(alien_0)

del alien_0['points'] # del Permanently deletes the value from the dictionary
print(alien_0)
