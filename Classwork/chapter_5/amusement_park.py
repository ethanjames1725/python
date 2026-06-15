"""Amusement park."""
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
