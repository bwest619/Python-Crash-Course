# this is an example of how not to copy a list. This copys a list without using a slice.

my_foods = ['pizza', 'filafel', 'carrot cake']

# this doesn't work
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\n")

print("My friend's favorite foods are:")
print(friend_foods)

# this example set friend_foods equal to my_foods. This syntax tells Python to connect the new variable friend_foods to the list that is already contained in my_foods, so now both variables point to the same list.
# As a result, when we add 'cannoli' to my_foods it will also appear in friend_foods, and vice versa
