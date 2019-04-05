# Try it yourself, page 214

import json

filename = 'favorite_num.json'
favorite_num = input("What is your favorite number? ")
with open(filename, 'w') as file_obj:
    json.dump(favorite_num, file_obj)

filename = 'favorite_num.json'
with open(filename) as file_obj:
    favorite_num = json.load(file_obj)
    print("I know your favorite number is: " + favorite_num)

