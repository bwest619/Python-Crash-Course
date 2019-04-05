# Creating and using a Class

# Each instance created from the dog class will store a name and an age, and we'll give the dog the ability...
# ...to sit() and roll_over()

class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age): # The __init__ method. A function that's part of a class is a method.
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# Making an instance from a class.
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Calling Methods. We can use dot notation to call any method defined in Dog
my_dog.sit()
my_dog.roll_over()
print("\n")

###################################################################################################

# Creating Multiple Instances.
# You can create as many instances from a  class as you need.
your_dog = Dog('lucy', 3) # Creating a second instance called 'your_dog"

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

