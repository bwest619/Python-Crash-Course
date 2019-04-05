# Using break to exit a loop

prompt = "\nPlease tell me the name of a city you have visited: "
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("\nI'd love to visit " + city.title() + "!")
