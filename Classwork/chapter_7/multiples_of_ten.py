"""
Asks the user to input a number and checks if it is a multiple of 10.
It prints a message indicating whether the number is a multiple or not.
"""
num = int(input("Please enter a number to check if it is a multiple of 10: "))

if num % 10 == 0:
    print(f"Yes! {num} is a multiple of 10!")
else:
    print(f"{num} is not a multiple of 10.")
