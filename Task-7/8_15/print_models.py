from printing_functions import print_models, show_completed_models

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
