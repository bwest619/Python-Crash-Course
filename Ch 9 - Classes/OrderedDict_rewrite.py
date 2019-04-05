# Try it yourself, page 186

from collections import OrderedDict

programming_words = OrderedDict()

programming_words['concatination'] = 'the operation of joining character strings end to end'
programming_words['tuple'] = 'a sequence of immutable Python objects'
programming_words['strings'] = 'can include numbers, letters, and various symbols and be enclosed by either double, or single quotes'
programming_words['if statement'] = 'conditionally executes a block of code, along with else, and elif'
programming_words['slice'] = 'a specific group of items in a list'

for word, definition in programming_words.items():
    print(word.title() + ": " + definition)

