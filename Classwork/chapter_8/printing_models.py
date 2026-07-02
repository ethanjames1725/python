"""Demonstrate importing functions from another module (printing_functions)
to simulate printing a queue of 3D designs and moving them into a
completed list."""
from printing_functions import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
