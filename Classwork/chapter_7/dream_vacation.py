"""summary"""
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
