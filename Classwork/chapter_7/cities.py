"""
Asks the user to enter the name of cities in a while loop and prints a
message for each city entered. The loop continues until the user
enters 'quit'.
"""

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break

    print(f"I'd love to go to {city.title()}!")
