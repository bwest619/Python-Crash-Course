# Exceptions

# Handling the zero division error exception
# Using try-except blocks when you think an error may occur - keeps the program running when you know..
# ..an error will occur

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print("\n")

######################################################################################################################

# Using exceptions to prevent crashes. This program doesn't have a way to handle if a user tries to divide a number...
# ...by zero. An error will occur if done so.
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# Here's the same program, but we implement a try-except block to handle an error we know can happen
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
