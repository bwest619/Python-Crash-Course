# Try it yourself, page 207

try:
    first_number = input("Give me a number: ")
    first_number = int(first_number)

    second_number = input("Give me another number: ")
    second_number = int(second_number)

except ValueError:
    print("Sorry, you must give me a number. Not a letter.")

else:
    answer = first_number + second_number
    print(answer)
