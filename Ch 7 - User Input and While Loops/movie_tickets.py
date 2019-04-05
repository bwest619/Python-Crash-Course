# Try it yourself, page 127

prompt = ("\nWhat is your age?\n")
prompt += ("Type 'quit' when you are done.\n")

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("Your ticket price is free!")
    elif age <= 12:
        print("Your ticket price is $10.")
    else:
        print("Your ticket price is $15.")
        