# Try it yourself, page 131

sandwich_orders = ['tuna', 'salami', 'club', 'pb&j', 'ham', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("I made your " + sandwich.title() + " sandwich.")
    finished_sandwiches.append(sandwich)

print("\nHere is all of the sandwiches that have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())