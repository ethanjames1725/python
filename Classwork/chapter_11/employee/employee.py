"""An Employee class that models an employee's name, salary, and raises."""


class Employee:
    """Models an employee."""

    def __init__(self, first, last, salary):
        """Initialises attributes."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        """Raises salary by 5000 by default but allows different ammounts."""
        self.salary += raise_amount
