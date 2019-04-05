# Try it yourself, page 127

toppings = ("\nWhat topping would you like to add to your pizza?")
toppings += ("\nWhen you are done, type 'quit'.")

while True:
    message = input(toppings)

    if message == 'quit':
        break
    else:
        print("\nI'm going to add " + message + " to your pizza!")
print("\n")

###################################################################

toppings = ("\nWhat topping would you like to add to your pizza?")
toppings += ("\nWhen you are done, type 'quit'.")

active = True
while active:
    message = input(toppings)

    if message == 'quit':
        active = False
    else:
        print("\nI'm going to add " + message + " to your pizza!")
print("\n")

####################################################################

toppings = ("\nWhat topping would you like to add to your pizza?")
toppings += ("\nWhen you are done, type 'quit'.")

message = ""

while message != 'quit':
    message = input(toppings)

    if message != 'quit':
        print("\nI'm going to add " + message + " to your pizza!")
