# simple if statements, and else if statements

age = 19
if age >= 18: # If this statement was false then the lines below would not be outputted by the program
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
print("\n")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
print("\n")
