# Try it yourself, page 178

class Users:
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


class Admin(Users):
    """Making a class for administrators"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initializing aspects of the administrators"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Prints privileges an admin has."""
        print("An admin has a set of privileges that can do any of the following:")
        for privilege in self.privileges:
            print(privilege)


administer = Admin('blaine', 'west', 'man in charge', 'bwest@bullshit.com', 'denver')
administer.privileges = ['can add post', 'can delete post', 'can ban user', 'can change your name to something silly']

administer.describe_user()
administer.greet_user()
administer.show_privileges()
