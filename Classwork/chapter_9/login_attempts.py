"""Summary"""


class User:
    """Summary"""

    def __init__(self, f_name, l_name, age, username):
        """Initialises attributes."""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\n{self.f_name.title()} {self.l_name.title()} {self.age} "
              f"{self.username}")

    def greet_user(self):
        """Prints a personalised greeting to the user."""
        print(f"Hello, {self.f_name.title()} {self.l_name.title()}.")

    def increment_login_attempts(self):
        """Increments login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0


user_0 = User('ethan', 'smith', 21, 'e_smith')
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)
