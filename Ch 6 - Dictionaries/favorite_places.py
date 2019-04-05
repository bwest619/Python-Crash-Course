# Try it yourself, page 115

favorite_places = {
    'blaine' : ['san diego', 'hawaii', 'sierras'],
    'broc' : ['oakland', 'denver', 'mountains'],
    'phil' : ['europe', 'asia', 'united states', 'africa'],
    'sasha' : ['san diego'],
    }

for people, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + people.title() + "'s favorite places are:")
    else:
        print("\n" + people.title() + "'s favorite place is:")

    for place in places:
        print("\t" + place.title())

############################################################

# for fun...
favorite_places = {
    'blaine' : ['san diego', 'hawaii', 'sierras'],
    'broc' : ['oakland', 'denver', 'mountains'],
    'phil' : ['europe', 'asia', 'united states', 'africa'],
    'sasha' : ['san diego'],
    }

print("\nThe people who I asked for their favorite places:")
for people, places in favorite_places.items():
    print("\t" + people.title())

for people, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + people.title() + "'s favorite places are:")
    else:
        print("\n" + people.title() + "'s favorite place is:")

    for place in places:
        print("\t" + place.title())