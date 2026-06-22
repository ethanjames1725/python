"""Calculates amusement park admission cost based on age, first with
a printed if/elif/else chain, then by assigning the cost to a
price variable using elif ranges that include a senior discount."""
age = 12

if age < 4:
    print("Your admission cost is R0.")
elif age < 18:
    print("Your admission cost is R25.")
else:
    print("Your admission cost is R40.")

print()

age = 12
price = 0

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is R{price}.")
