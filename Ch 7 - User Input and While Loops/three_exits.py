# Try it yourself, page 128

prompt = ("\nWhat is your age?\n")
prompt += ("Type 'quit' when you are done.\n")

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket price is free!")
        elif age <= 12:
            print("Your ticket price is $10.")
        else:
            print("Your ticket price is $15.")

###############################################################

prompt = ("\nWhat topping would you like to add to your pizza?")
prompt += ("\nWhen you are done, type 'quit'.")

while True:
    toppings = input(prompt)

    if toppings != 'quit':
        print("\nI'm going to add " + toppings + " to your pizza!")
    else:
        break

#########################################################################

prompt = ("\nWhat topping would you like to add to your pizza?")
prompt += ("\nWhen you are done, type 'quit'.")

toppings = ""
while toppings != 'quit':
    toppings = input(prompt)

    if toppings != 'quit':
        print("\nI'm going to add " + toppings + " to your pizza!")