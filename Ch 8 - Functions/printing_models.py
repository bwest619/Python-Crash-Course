# Modifying a list in a function

# Start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("\nPrinting model: " + current_design.title())

    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model.title())

###########################################################################################

# Reorganizing the previous code by writing two functions, making the code more efficient
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
        Move each design to completed_models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("\nPrinting model: " + current_design.title())
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model.title())

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)