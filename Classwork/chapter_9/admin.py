"""Summary"""


class User:
    """Summary"""

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


class Privileges:
    """Summary"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Prints list of privileges."""
        print("\nAdmin privileges include:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")


class Admin(User):
    """Summary"""

    def __init__(self, f_name, l_name, age, username):
        """Summary"""
        super().__init__(f_name, l_name, age, username)
        self.privileges = Privileges()


admin_0 = Admin('ethan', 'smith', 21, 'e_smith')
admin_0.describe_user()
admin_0.privileges.show_privileges()
