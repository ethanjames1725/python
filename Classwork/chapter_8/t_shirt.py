"""summary"""


def make_shirt(size, text):
    """Display the size of the shirt and a message that should be
    printed on the shirt."""
    print(f"\nThe size of the shirt is a {size}.")
    print(f"The message to be printed onto the shirt is: {text}.")


make_shirt('medium', 'happy smiles')
make_shirt(size='large', text='superman')
