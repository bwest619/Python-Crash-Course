# try it yourself, page 69

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())
print("\n")

print("My friend's favorite foods are:")
for foods in friend_foods:
    print(foods.title())
print("\n")

print("My top three favorite foods are:")
for food in my_foods[:3]:
    print(food.title())
print("\n")

print("My friend's last favorite food is:")
for foods in friend_foods[3:]:
    print(foods.title())
print("\n")
