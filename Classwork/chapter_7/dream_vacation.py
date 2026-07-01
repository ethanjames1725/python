"""
Creates a dictionary of dream vacations based on user input and displays
the results. It prompts the user for their name and dream vacation
destination, and stores the responses in a dictionary. The user can continue
to add more responses until they choose to stop. Finally, the program prints
the results of the poll, showing each person's name and their dream vacation
destination.
"""
dreams = {}

while True:
    name = input("\nWhat is your name? ")
    vacay = input("If you could visit one place in the world for a dream "
                  "getaway, where would you go? ")

    dreams[name] = vacay

    repeat = input("Would you like another person to respond? (yes/no) ")
    if repeat.lower() == 'no':
        break

print("\n--- Poll Results ---")
for name, vacay in dreams.items():
    print(f"{name.title()}'s dream vacation is going to {vacay.title()}!")
