# Try it yourself, page 115

pets = []

pet = {
    'name' : 'gizmo',
    'type' : 'cat',
    'owner' : 'blaine',
    }
pets.append(pet)

pet = {
    'name' : 'raisin',
    'type' : 'cat',
    'owner' : 'broc',
    }
pets.append(pet)

pet = {
    'name' : 'trixie',
    'type' : 'dog',
    'owner' : 'sasha',
    }
pets.append(pet)

for pet in pets:
    print("\nThis is what I know about " + pet['name'].title() + ":")

    for key, value in pet.items():
        print("\t" + key.title() + ": " + value.title())
        


