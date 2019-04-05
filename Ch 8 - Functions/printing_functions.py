# Copying the functions from printing_models.py in to this new file
# Using this file to import the functions in to the program printing_models_2.py for Try it yourself, page 159

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