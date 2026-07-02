"""Demonstrate collecting an arbitrary number of positional arguments
with *items, including unpacking an existing list of fillings into
the function call with the * operator."""


def make_sandwich(*items):
    """
    Print a summary from a list of items of the sandwich that's being ordered.
    """
    print("\nSandwich fillings:")
    for item in items:
        print(f"- {item}")


sandwich_0 = ['chicken', 'mayo']

make_sandwich('ham', 'cheese')
make_sandwich(*sandwich_0)
make_sandwich('ham', 'tomato', 'cheese')
