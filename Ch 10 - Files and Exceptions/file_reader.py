# Reading from a file

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents) # Can also use the .rstrip() method as read() always sends one blank line as the last line when used

    print("\n" + contents.rstrip())
    print("\n")

###################################################################################################################

# Reading line by line.
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

##################################################################################################################

# This example stores the lines in a list inside the with block and then prints the lines outside the with block
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() # takes each line from the file and stores it in a list. List is stored in 'lines'.

for line in lines:
    print(line.rstrip())
print("\n")

#####################################################################################################################

# After you've read a file into memory, you can do whatever you want with the data
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print("\n")
print(len(pi_string))
print("\n")

# Same example, only this time we're getting rid of the white space on the left side as well
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print("\n")
print(len(pi_string))
print("\n")

##################################################################################################################



