# Try it yourself, page 154

def make_sandwich(*items):
    """Printing a summary of the sandwich being ordered"""
    print("\nMaking your sandwich with the following items: ")
    for item in items:
        print(item)


make_sandwich('ham', 'cheese', 'lettuce')
print("\n")

make_sandwich('peanut butter', 'jelly')
print("\n")

make_sandwich('bacon', 'tomato', 'lettuce')
