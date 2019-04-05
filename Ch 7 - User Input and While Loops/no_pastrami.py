# Try it yourself, page 131

sandwich_orders = ['tuna', 'pastrami', 'salami', 'club', 'pastrami', 'pb&j', 'pastrami', 'ham', 'turkey']
print(sandwich_orders)
finished_sandwiches = []

print("\nWe apologize as the deli has run out of Pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I am making your " + current_sandwich.title())

    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that are finished: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

