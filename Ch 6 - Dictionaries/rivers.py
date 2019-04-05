# Try it yourself, page 108

rivers = {
    'nile' : 'egypt',
    'zambezi' : 'africa',
    'ganges' : 'india',
    'mississippi' : 'united states',
    'yangtze' : 'china',
}

for river, location in rivers.items():
    print("The " + river.title() + " river runs through " + location.title() + ".")
print("\n")

print("The following rivers are included in this dictionary:")
for river in rivers.keys():
    print(river.title())
print("\n")

print("The following countries are included in this data set:")
for location in rivers.values():
    print(location.title())
