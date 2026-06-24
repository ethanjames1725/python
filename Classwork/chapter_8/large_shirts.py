"""summary"""


def make_shirt(size='large', text='I love Python'):
    """Display the size of the shirt and a message that should be
    printed on the shirt."""
    print(f"\nThe size of the shirt is a {size}.")
    print(f"The message to be printed onto the shirt is: {text}.")


make_shirt()
make_shirt(size='medium')
make_shirt(size='small', text='I love Batman')
