"""Exercises for checking pizza toppings using conditionals and lists."""
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Checking whether a value is in a list:
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(f"\nRequested Toppings:{requested_toppings}\n")
print("'mushrooms' in requested_toppings: "
      f"{'mushrooms' in requested_toppings}")
print("'pepperoni' in requested_toppings: "
      f"{'pepperoni' in requested_toppings}")

print("\nMultiple if statement:\n")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!\n")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("\nUsing multiple lists:\n")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
