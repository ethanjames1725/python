"""Summary"""

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
