# Try it yourself, page 93

current_users = ['blaine', 'broc', 'sasha', 'robert', 'ranae']

new_users = ['alex', 'broc', 'austin', 'robert', 'trevor']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("I'm sorry, the username " + new_user + " is already taken. Please pick a different username.")
    else:
        print("The username " + new_user + " is available!")

