# Try it yourself, page 121

reservation = input("How many people, total, will be in your group for dinner tonight? ")
reservation = int(reservation)

if reservation > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")
