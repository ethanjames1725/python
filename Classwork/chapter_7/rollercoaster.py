"""
Prompts the user for their height in centimetres and checks if they
are all tall enough to ride a rollercoaster. It prints a message indicating
whether they are tall enough to ride or if they will need to wait until
they are a little older.
"""
height = int(input("How tall are you, in centimetres? "))

if height >= 120:
    print("\nYou're tall enough to ride!")
else:
    print(("\nYou'll be able to ride when you're a little older."))
