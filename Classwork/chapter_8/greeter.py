"""summary"""
def greet_user(username):
    """Display simple greeting."""
    print(f"Hello, {username.title()}")

greet_user(input("What is your name? "))
