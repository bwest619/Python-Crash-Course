# Try it yourself, page 171

class Users():
    """Making a class for user profiles."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Print a description of the user"""
        print("\n" + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Location: " + self.location)

    def greet_user(self):
        """Prints a greeting to the user"""
        print("Welcome, " + self.username + "!")

    def increment_login_attempts(self):
        """Incrementing the value of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = Users('blaine', 'west', 'bwest', 'bwest@yahoo.com', 'denver')

print("\n")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("Login attempts: " + str(user_1.login_attempts))

user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("Login attempts: " + str(user_1.login_attempts))

user_1.reset_login_attempts()
print("Login attempts: " + str(user_1.login_attempts))


