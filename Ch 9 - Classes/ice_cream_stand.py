# Try it yourself, page 178

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints a message describing the name and cuisine of the restaurant"""
        print(self.restaurant_name.title() + " is a " + self.cuisine_type.title() + " style restaurant.")

    def open_restaurant(self):
        """Message stating the restaurant is open"""
        print(self.restaurant_name.title() + " is currently open!")


class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Represents aspects to an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def stand_flavors(self):
        """Prints the flavors of ice cream available"""
        print("\nWe have the following flavors:")
        for flavor in self.flavors:
            print(flavor.title())


yogurt_mill = IceCreamStand('yogurt mill')
yogurt_mill.flavors = ['chocolate', 'vanilla', 'rocky road', 'mint']

yogurt_mill.describe_restaurant()
yogurt_mill.stand_flavors()
