# Try it yourself, page 102

programming_words = {
    'concatenation' : 'the operation of joining character strings end to end',
    'tuple' : 'a sequence of immutable Python objects',
    'strings' : 'can include numbers, letters, and various symbols and be enclosed by either double, or single quotes',
    'if statement' : 'conditionally executes a block of code, along with else, and elif',
    'slice' : 'a specific group of items in a list',
    }

print("Concatenation: " + programming_words['concatenation'])
print("Tuple: " + programming_words['tuple'])
print("Strings: " + programming_words['strings'])
print("If Statements: " + programming_words['if statement'])
print("Slice: " + programming_words['slice'])
print('\n')

# Another way to do this...
programming_words = {
    'concatenation' : 'the operation of joining character strings end to end',
    'tuple' : 'a sequence of immutable Python objects',
    'strings' : 'can include numbers, letters, and various symbols and be enclosed by either double, or single quotes',
    'if statement' : 'conditionally executes a block of code, along with else, and elif',
    'slice' : 'a specific group of items in a list',
    }

word = 'concatenation'
print(word.title() + ": " + programming_words[word])
word = 'tuple'
print(word.title() + ": " + programming_words[word])
word = 'strings'
print(word.title() + ": " + programming_words[word])
word = 'if statement'
print(word.title() + ": " + programming_words[word])
word = 'slice'
print(word.title() + ": " + programming_words[word])

