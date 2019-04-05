# Try it yourself, page 199

filename = 'programming_poll.txt'

print("Enter 'q' at any time to end this poll.")
while True:
    reason = input("Why do you like programming? ")

    if reason == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(reason + "\n")

#############################################################################################################

# Another way is to create an empty list, append to the list, and then write a for loop to add the list to the file

filename = 'programming_poll.txt'

responses = []
while True:
    response = input("Why do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else give a reason? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as file_object:
    for response in responses:
        file_object.write(response + "\n")
