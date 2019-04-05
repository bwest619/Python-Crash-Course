# Checking for inequality.
# When you want to determine two values are not equal, you can present it as (!=).
# The ! symbol represents 'not'

requested_topping = 'mushrooms'

if requested_topping != 'anchovies': # If requested topping does not equal anchovies, print "Hold the anchovies!"
    print("Hold the anchovies!")
print("\n")

# This next example tests for multiple conditions using the if statement
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
print("\n")

# This example shows that the previous example would not work using an if-elif statement.
# The code would stop running after only one test passes.
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings: # This passes and therefore cancels any more attempts in this type of statement
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings: # Will not pass as 'mushrooms' already passed the test. Shows this example would not work for this type of program
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
print("\n")