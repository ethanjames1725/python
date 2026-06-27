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


class IceCreamStand(Restaurant):
    """Summary"""

    def __init__(self, restaurant_name, cuisine_type):
        """Summary"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['vanilla', 'chocolate', 'strawberry']

    def show_flavours(self):
        """Prints ice cream flavours."""
        print("\nThe ice cream flavours are:")
        for flavour in self.flavours:
            print(f"\t- {flavour}")


ice_cream_stand = IceCreamStand('I Scream', 'Ice Cream')
ice_cream_stand.show_flavours()
