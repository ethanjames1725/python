"""Checks voting eligibility based on age, first with a simple if
statement and then with an if/else for an underage voter."""
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
