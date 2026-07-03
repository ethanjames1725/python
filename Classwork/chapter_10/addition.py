"""Repeatedly prompt the user for two numbers and print their sum.

Handles non-numeric input with a try/except block and exits the
loop when the user enters 'q' for either number.
"""

while True:
    try:
        print("\nPlease enter two numbers to add together. "
              "(enter 'q' to quit)")

        num_1 = input("First number: ")
        if num_1 == 'q':
            break
        num_1 = int(num_1)

        num_2 = input("Second number: ")
        if num_2 == 'q':
            break
        num_2 = int(num_2)

    except ValueError:
        print("Sorry, please enter a number value.")

    else:
        print(f"The sum of your numbers is: {num_1 + num_2}")
