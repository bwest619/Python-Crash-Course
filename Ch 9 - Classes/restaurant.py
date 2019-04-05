# Try it yourself, page 166

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


restaurant = Restaurant('pizza hut', 'american')
print("The restaurant's name is " + restaurant.restaurant_name.title() + ".")
print("It is an " + restaurant.cuisine_type.title() + " style restaurant.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
