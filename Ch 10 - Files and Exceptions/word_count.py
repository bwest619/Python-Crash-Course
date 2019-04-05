# Working with multiple files

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in a file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has approximately " + str(num_words) + " words.")


filename = 'alice.txt'
count_words(filename)
print("\n")

filename = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for files in filename:
    count_words(files)

# Failing silently... If you don't want a user to know an error has occurred using a try- except block...
# ...Python has a 'pass' statement that tells it to do nothing in the block.
# The 'pass' statement goes in the except FileNotFoundError block.

