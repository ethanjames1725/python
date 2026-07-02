"""Module defining make_pizza(), which accepts a required size and
an arbitrary number of toppings (*toppings) and prints a summary of
the pizza being made. Meant to be imported by making_pizzas.py."""


# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(size, *toppings):
    """Summarise the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza(16,'pepperoni')
# make_pizza(17, 'mushrooms', 'green peppers', 'extra cheese')
