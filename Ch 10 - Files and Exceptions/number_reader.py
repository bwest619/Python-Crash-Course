# Writing a program that uses json.load() to read a list of numbers in a file we created with json.dump()

import json

filename = 'numbers.json'

with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)
