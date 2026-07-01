"""Summary"""

used_colours = ['blue', 'yellow', 'red', 'black', 'white', 'brown']
confirmed_colours = []

while used_colours:
    current_colour = used_colours.pop()
    print(f"Verifying colours: {current_colour.title()}")
    confirmed_colours.append(current_colour)

print("\nThe following colours have been confirmed:")
for confirmed_colour in confirmed_colours:
    print(confirmed_colour.title())

print(used_colours)
print(confirmed_colours)


# # 2. Removing All Instances of Specific Values from a List

# cars = ['Benz', 'BMW', 'Benz', 'Polo', 'BMW', 'Honda', 'BMW']

# print("\nOriginal list of cars:", cars)

# while 'BMW' in cars:

#     cars.remove('BMW')  # Remove first occurrence of 'BMW'

# while 'Benz' in cars:

#     cars.remove('Benz')  # Remove first occurrence of 'Benz'

# print("Updated list of pets:", cars)

#############################################################################

# 3. Filling a Dictionary with User Input

# Filling a Dictionary with User Input

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False  # End the poll if the user types 'no'


# Show the poll results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
