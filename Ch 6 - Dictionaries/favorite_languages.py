# You can also use a dictionary to store different kinds of information about one object

favorite_languages = {'jen' : 'python', 'sarah': 'c', 'edward' : 'ruby', 'phil' : 'python'}

# When you know a dictionary is going to take up more than one line... write it as so...
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# To break up a long print statement in to a bunch of lines you can do like so...
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")
print('\n')




# Looping through the dictionary
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

for name, language in favorite_languages.items():
    print("\nName: " + name.title())
    print("Language: " + language.title())
print("\n")

# or..
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
print("\n")




# Looping through all the keys in a dictionary when you don't need the key's value
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

for name in favorite_languages.keys():
    print(name.title())
print("\n")

# or...
for name in favorite_languages: # works the same because looping through the keys is the default behavior in Python...
    print(name)                 # ...when looping through a dictionary
print("\n")




# Accessing a value associated with any key you care about inside the loop by using a current key
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + ".")
        # This example confused me. To print the value you use the dictionary name followed by name as the key in brackets



# Using the keys method to find out if a person was polled
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")
print("\n")



# Looping through a dictionaries keys in order
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
print("\n")




# Looping through all the values stored in a dictionary without listing any of the keys
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values(): # This example doesn't check for repeats
    print(language.title())
print("\n")

# To see each language chosen without repetition, we can use a 'set'
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): # Shows no repetition in languages mentioned
    print(language.title())
print("\n")

##################################################################

# Making a list inside a dictionary
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() +"'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
print("\n")

#################################################################

# Just practicing here. Adding an if statement at the beginning of the for loop...
# To detect if a person likes more than one language or not, and then changing the text to fit
avorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() +"'s favorite languages are:")
    else:
        print("\n" + name.title() + "'s favorite language is:")

    for language in languages:
        print("\t" + language.title())
print("\n")
