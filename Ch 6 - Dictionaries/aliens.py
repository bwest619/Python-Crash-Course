# Nesting: storing a set of dictionaries in a list, or a list of items as a value in a dictionary
# With nesting, you can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even a...
# ...dictionary inside a dictionary.

# A list of dictionaries.
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print("\n")

#######################################################################################

# Using range() to create a fleet of 30 aliens
# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[ : 5]:
    print(alien)
print("...")

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
print("\n")

#######################################################################################

# Working with a set of aliens in a list: Changing the first three aliens to yellow...
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
print("\n")

for alien in aliens[:3]: # Changing the first three aliens to yellow
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# Show the first 5 aliens
for alien in aliens[ : 5]:
    print(alien)
print("...")

################################################################################################

# Writing the same code as above only we're adding an elif code to the block to change any yellow aliens to red

# Working with a set of aliens in a list: Changing the first three aliens to yellow...
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
print("\n")

for alien in aliens[:3]: # Changing the first three aliens to yellow
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow': # Would change yellow aliens to red aliens if there were any in the first 3
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the first 5 aliens
for alien in aliens[ : 5]:
    print(alien)
print("...")