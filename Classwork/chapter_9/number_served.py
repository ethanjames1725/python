"""Summary"""


class Restaurant:
    """Summary"""

    def __init__(self, restaurant_name, cuisine_type):
        """Stores name and cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant information."""
        print(f"{self.restaurant_name}: {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, num_served):
        """Sets the number of customers that have been served."""
        self.number_served = num_served

    def increment_number_served(self, served):
        """Increment that number of customers who have been served."""
        self.number_served += served


restaurant = Restaurant('Pomodoro', 'Italian')
print(restaurant.number_served)

restaurant.set_number_served(10)
print(restaurant.number_served)

restaurant.increment_number_served(15)
print(restaurant.number_served)
