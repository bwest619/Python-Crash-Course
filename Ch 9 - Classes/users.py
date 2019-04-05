# Try it yourself, page 166

class Users():
    """Making a class for user profiles."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Print a description of the user"""
        print("\n" + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Location: " + self.location)

    def greet_user(self):
        """Prints a greeting to the user"""
        print("Welcome, " + self.username + "!")


user_1 = Users('blaine', 'west', 'bwest', 'bwest@yahoo.com', 'denver')
user_2 = Users('broc', 'west', 'brocman', 'brocman@yahoo.com', 'denver')
user_3 = Users('tyrion', 'lannister', 'righthandman', 'bigman@gmail.com', 'dragonstone')

user_1.describe_user()
user_1.greet_user()
print("\n")
user_2.describe_user()
user_2.greet_user()
print("\n")
user_3.describe_user()
user_3.greet_user()
