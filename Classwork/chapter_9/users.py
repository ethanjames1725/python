"""A simple User class demonstrating creation of multiple instances."""


class User:
    """Represents a user with basic profile information."""

    def __init__(self, f_name, l_name, age, username):
        """Initialises attributes."""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.username = username

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\n{self.f_name.title()} {self.l_name.title()} {self.age} "
              f"{self.username}")

    def greet_user(self):
        """Prints a personalised greeting to the user."""
        print(f"Hello, {self.f_name.title()} {self.l_name.title()}.")


user_0 = User('ethan', 'smith', 21, 'e_smith')
user_0.describe_user()
user_0.greet_user()

user_1 = User('john', 'snow', 25, 'watcher')
user_1.describe_user()
user_1.greet_user()

user_2 = User('lady', 'gaga', 30, 'pokerface')
user_2.describe_user()
user_2.greet_user()
