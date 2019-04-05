# Try it yourself, page 208

print("Enter 'q' at any time to quit.")
while True:
    try:
        first_number = input("Give me a number: ")
        if first_number == 'q':
            break
        first_number = int(first_number)

        second_number = input("Give me another number: ")
        if second_number == 'q':
            break
        second_number = int(second_number)

    except ValueError:
        print("Sorry, you must give me a number. Not a letter.")

    else:
        answer = first_number + second_number
        print(answer)