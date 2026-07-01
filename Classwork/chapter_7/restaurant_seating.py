"""
Asks the user for the number of people in their dinner group and checks if
the group is larger than 8. It prints a message indicating whether the group
will need to wait for a table or if their table is ready.
"""
num_people = int(input("How many people are in your dinner group? "))

if num_people > 8:
    print(f"Please wait while we find you suitable a table for {num_people}.")
else:
    print(f"Your table for {num_people} is ready!")
