# Try it yourself, page 171

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Prints a message describing the name and cuisine of the restaurant"""
        print(self.restaurant_name.title() + " is a " + self.cuisine_type.title() + " style restaurant.")


    def open_restaurant(self):
        """Message stating the restaurant is open"""
        print(self.restaurant_name.title() + " is currently open!")


    def set_number_served(self, served):
        """Sets the number of customers that have been served"""
        self.number_served = served
        print("Customers served: " + str(self.number_served))


    def increment_number_served(self, additional_served):
        """Increments the total customers served"""
        self.number_served += additional_served


restaurant = Restaurant('pizza hut', 'pizza')
print(restaurant.number_served)
restaurant.number_served = 13
print(restaurant.number_served)
print("\n")

restaurant.set_number_served(425)
print("\n")

restaurant.increment_number_served(127)
print(restaurant.number_served)
