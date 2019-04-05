# the if-elif-else chain

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
print("\n")

# You can set the price inside the if-elif-else block to make more concise
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
print("\n")

# You can use multiple elif statements in a block. Here we add an extra one to the previous statements.
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")
print("\n")

# Python does not require an else statement at the end of an if-elif-else block.
# Sometimes it is more clear to omit an else statement by implementing a final elif instead.
# However, by doing so there is no "catchall" by using an else. Every piece of code must pass a specific test to execute
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
print("\n")