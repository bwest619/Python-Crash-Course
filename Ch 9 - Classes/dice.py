# Try it yourself, page 186

from random import randint

class Die:
    def __init__(self, sides=6):
        """Initializes the die."""
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides of the die."""
        return randint(1, self.sides)


# Rolling a 6 sided die 10 times
my_dice = Die()
results = []

for roll_num in range(10):
    result = my_dice.roll_die()
    results.append(result)
print(results)

# Making a 10 sides die and rolling 10 times
dice2 = Die(sides=10)
results2 = []

for roll_num2 in range(10):
    result2 = dice2.roll_die()
    results2.append(result2)
print(results2)

# Making a 20 sided die and rolling 10 times
dice3 = Die(sides=20)
results3 = []

for roll_num3 in range(10):
    result = dice3.roll_die()
    results3.append(result)
print(results3)


