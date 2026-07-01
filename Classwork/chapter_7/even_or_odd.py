"""
Prompts the user to enter a number and then tells the user whether the
number is even or odd.
"""
number = int(input("Enter a number, and I will "
                   "tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
