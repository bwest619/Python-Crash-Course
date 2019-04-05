# using the range() function

for value in range(1, 5):
    print(value)
print("\n")

for value in range(1, 6):
    print(value)
print("\n")

# using range to make a list of numbers
numbers = list(range(1, 5))
print(numbers)
print("\n")

numbers = list(range(1, 6))
print(numbers)
print("\n")

even_numbers = list(range(2, 11, 2)) # prints even numbers starting at 2 that increase by 2 until it reaches the final value of 11, hence the 2 after the 11
print(even_numbers)
print("\n")

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
print("\n")

# can write the previous code more precisely as follows..
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print("\n")

#using min, max, and sum to find the minimum number, the maximum number, and the sum of the numbers in the list
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
