"""
Prompts the user for the type of rental car they would like and prints
a message indicating that the program will check for availability of that car.
"""
rental = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {rental.title()}.")
