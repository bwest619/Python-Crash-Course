# Try it yourself, page 199

filename = 'guest_book.txt'

print("Enter 'q' at any time if there are no other names to give.")

while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name.title() + "\n")
        print("Hello, " + name.title() + ", you have been added to the guest book!")







