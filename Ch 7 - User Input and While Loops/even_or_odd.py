# Using the modulus operator to determine if a number is even or odd
# Also, the modulus operator divides two numbers and ONLY gives you the remainder. Nothing else

number = input("Enter a number and I'll tell you whether it is even or odd. ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
