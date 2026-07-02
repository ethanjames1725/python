"""Demonstrate passing a list to a function by greeting every
username in a list of names."""


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
