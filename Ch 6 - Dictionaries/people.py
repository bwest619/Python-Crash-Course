# Try it yourself, page 114

people = []

person = {
    'first_name' : 'blaine',
    'last_name' : 'west',
    'age' : 36,
    'city' : 'denver',
    }
people.append(person)

person = {
    'first_name' : 'broc',
    'last_name' : 'west',
    'age' : 33,
    'city' : 'denver',
    }
people.append(person)

person = {
    'first_name' : 'sasha',
    'last_name' : 'west',
    'age' : 29,
    'city' : 'san diego',
    }
people.append(person)

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    print("\n" + full_name.title() + " is " + str(person['age']) + " years old and lives in the city of " + person['city'].title() + ".")

#######################################################################################################

# Can also do the for loop as so

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    age = str(person['age'])
    city = person['city']
    print("\n" + full_name.title() + " is " + age + " years old and lives in the city of " + city.title() + ".")
    