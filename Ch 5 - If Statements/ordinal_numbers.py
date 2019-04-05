# Try it yourself, page 93

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in numbers:
    if number == '1':
        print(number + "st")
    elif number == '2':
        print(number + 'nd')
    elif number == '3':
        print(number + "rd")
    else:
        print(number + 'th')
print("\n")

# My work up top definitely works. This next example shows a better, more simple way of writing the same code
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")
print("\n")

# My example up top doesn't need '' around the numbers. This example is the better example of my original work
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")