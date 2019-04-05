# try it yourself, page 50
locations = ['greece', 'scotland', 'italy', 'puerto rico', 'hawaii']

print(locations)

print("\nHere is the list in alphabetical order:")
print(sorted(locations))

print("\nHere is the original order again:")
print(locations)

print("\nHere is the list in reverse alphabetical order:")
print(sorted(locations, reverse = True))

print("\nHere is the list in the original order once again:")
print(locations)

locations.reverse()
print("\nHere is the list in a reverse order:")
print(locations)

locations.reverse()
print("\nHere is the list reversed back to its original order:")
print(locations)

locations.sort()
print("\nHere is the list sorted in alphabetical order:")
print(locations)

locations.sort(reverse = True)
print("\nHere is the list sorted in reverse alphabetical order:")
print(locations)
