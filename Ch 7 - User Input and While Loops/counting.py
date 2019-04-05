# Playing with while loops

# The following while loop counts from 1 to 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print("\n")

#####################################################################

# Using 'continue' in a loop

current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    print(current_number)

print("\n")

######################################################################

# Avoiding infinite loops - stopping a while loop so it won't continue to run forever

x = 1
while x <= 5:
    print(x)
    x += 1 # Omitting this line will cause this program to run forever. 'CTRL-C' ends the loop, stupid.




