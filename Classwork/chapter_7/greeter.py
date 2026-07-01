"""
Prompts the user for their name and age, and prints a greeting message.
"""
name = input("Please enter your name: ")
print(f"\nHello, {name.title()}")

prompt = "If you share your name, we can personalise the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print((f"\nHello, {name.title()}"))

age = input("How old are you? ")
print(age)

age = input("How old are you? ")
age = int(age)
print(age >= 18)
