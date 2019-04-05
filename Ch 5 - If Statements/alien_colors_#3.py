# Try it yourself, page 88

alien_color = 'yellow'

if alien_color == 'green':
    print("You've just earned 5 points!\n")
elif alien_color == 'yellow':
    print("You've just earned 10 points!\n")
else:
    print("You've just earned 15 points!\n")

alien_color = 'red'

if alien_color == 'green':
    print("You've just earned 5 points!\n")
elif alien_color == 'yellow':
    print("You've just earned 10 points!\n")
elif alien_color == 'red':
    print("You've just earned 15 points!\n")

alien_color = 'green'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

print("You've scored " + str(points) + " points!\n")