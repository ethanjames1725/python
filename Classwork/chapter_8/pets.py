"""Demonstrate positional and keyword arguments, plus a default
parameter value, by describing a pet's type and name."""


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print((f"My {animal_type}'s name is {pet_name.title()}."))


describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster')
