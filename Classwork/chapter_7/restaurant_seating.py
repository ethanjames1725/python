"""Summary"""
num_people = int(input("How many people are in your dinner group? "))

if num_people > 8:
    print(f"Please wait while we find you suitable a table for {num_people}.")
else:
    print(f"Your table for {num_people} is ready!")
