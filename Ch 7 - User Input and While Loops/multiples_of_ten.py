# Try it yourself, page 121

number = input("Give me a number and I will tell you whether it is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is a multiple of 10!")
else:
    print("The number " + str(number) + " is not.")
