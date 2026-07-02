"""Repeatedly prompt the user for a first and last name, format the
full name with get_formatted_name(), and print a greeting. The loop
exits when 'q' is entered for either name."""


def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# def greet_user(username):
#     """Display simple greeting."""
#     print(f"Hello, {username.title()}")

# greet_user(input("What is your name? "))


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name.lower() == 'q':
        break

    l_name = input("Last name: ")
    if l_name.lower() == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
