"""Module defining print_models() and show_completed_models(), which
together simulate a 3D printing queue: designs are moved one by one
from an unprinted list to a completed list. Meant to be imported by
printing_models.py."""


def print_models(unpr_designs, compl_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unpr_designs:
        current_design = unpr_designs.pop()
        print(f"Printing model: {current_design}")
        compl_models.append(current_design)


def show_completed_models(compl_models):
    """
    Show all models that were printed.
    """
    print("\nThe following models have been printed:")
    for completed_model in compl_models:
        print(completed_model)
