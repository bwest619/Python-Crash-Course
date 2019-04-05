# making a list of squared values

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
print("\n")

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print("\n")

# the following example builds the same list of square numbers but uses a list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)
print("\n")

