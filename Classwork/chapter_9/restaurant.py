"""Summary"""


class Restaurant:
    """Summary"""

    def __init__(self, restaurant_name, cuisine_type):
        """Stores name and cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints restaurant information."""
        print(f"{self.restaurant_name}: {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open.")


restaurant = Restaurant('Pomodoro', 'Italian')
print(f"The restaurant's name is {restaurant.restaurant_name}.")
print(f"The cuisine type is {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant('Nandos', 'Fast Food')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('FishyFood', 'Seafood')
restaurant_2.describe_restaurant()
