# Greeting a user who comes back to a program when their name has been stored

import json

filename = 'username.json'
with open(filename) as file_obj:
    username = json.load(file_obj)
    print("Welcome back, " + username + "!")
