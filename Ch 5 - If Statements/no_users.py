# Try it yourself, page 93

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello " + username + ", would you like to see a status report?")
        else:
            print("Hello, " + username.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")
    