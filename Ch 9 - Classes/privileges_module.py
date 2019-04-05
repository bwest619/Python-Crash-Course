"""A user with administrative privileges"""

from user_module import Users

class Privileges:
    """Making a class to hold the list of privileges for admins."""
    def __init__(self, privileges=[]):
        """Initialize the set of privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Prints privileges an admin has."""
        print("An admin has a set of privileges that can do any of the following:")
        for privilege in self.privileges:
            print(privilege)


class Admin(Users):
    """Making a class for administrators"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initializing aspects of the administrators"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()
