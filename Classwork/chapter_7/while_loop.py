"""
Demonstrates the use of while loops by prompting the user to keep going or end
the loop.
"""

active = True

while active:
    user_input = input("Do you want to keep going? (yes/no): ").lower()

    if user_input == 'no':
        active = False
        print("Goodbye!")
    elif user_input == 'yes':
        print("Lets keep going!")
