# Try it yourself, page 208

filename = ['cats.txt', 'dogs.txt']

for filenames in filename:
    try:
        with open(filenames) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry, that file does not exist.")
    else:
        print(contents)
    