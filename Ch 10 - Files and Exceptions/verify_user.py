# Try it yourself, page 214

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
    return username


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        message = input("Is " + username + " your correct username? (y/n)")
        if message == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you return, " + username + "!")

greet_user()
