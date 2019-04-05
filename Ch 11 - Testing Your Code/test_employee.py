# Try it yourself, page 228
# Test case for employee.py

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test the employee class from employee.py"""

    def setUp(self):
        """Setting up an employee for the test"""
        self.blaine = Employee('blaine', 'west', 32000)

    def test_give_default_raise(self):
        """Giving default raise."""
        self.blaine.give_raise()
        self.assertEqual(self.blaine.salary, 37000)

    def test_give_custom_raise(self):
        """Giving custom raise."""
        self.blaine.give_raise(amount=7000)
        self.assertEqual(self.blaine.salary, 39000)


if __name__ == '__main__':
    unittest()


