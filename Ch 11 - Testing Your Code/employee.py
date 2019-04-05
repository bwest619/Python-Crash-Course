# Try it yourself, page 228

class Employee:
    """A class defining an employee."""

    def __init__(self, first, last, salary):
        """Initialize an employee attributes."""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Giving a raise that adds 5000 to annual salary by default, but also allows you to give a different amount"""
        self.salary += amount
