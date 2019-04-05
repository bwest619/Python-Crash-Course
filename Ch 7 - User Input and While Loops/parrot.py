# Using the input() function

message = input("Tell me something, and I will repeat it back to you: ")
print(message)
print("\n")

#####################################################################

# While loop... letting the user choose when to stop the program
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

######################################################################

# Using a simple if test so that when the user types 'quit' the word 'quit' isn't printed as well
# Using the same program

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

###################################################################

# Using a 'Flag' - a variable that determines whether or not the entire program is active
# We can write our programs so they run while the flag is set to True and stop running when it sets to False

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True # active is the variable used as the flag
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
        

