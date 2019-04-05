# copying a list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # you can copy a list that includes the entire original list by omitting the first index and the second index '[:]'

print("My favorite foods are:")
print(my_foods)
print("\n")

print("My friend's favorite foods are:")
print(friend_foods)
print("\n")

# we are going to prove the lists are different by adding an item to each list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\n")

print("My friend's favorite foods are:")
print(friend_foods)
print("\n")
