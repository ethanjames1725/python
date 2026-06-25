"""Summary"""


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
