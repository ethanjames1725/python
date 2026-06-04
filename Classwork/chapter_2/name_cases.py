#Summary: This code prompts the user for their name using input() and stores it in the variable name, 
# then prints it three times using string methods: 
# .lower() makes every letter lowercase, .upper() makes every letter uppercase, 
# and .title() capitalizes the first letter of each word. 
# The + operator is used to join the label string with the transformed name before printing.

name = input("What is your name? ")
print("Your name in lowercase is " + name.lower())
print("Your name in uppercase is " + name.upper())
print("Your name in title case is " + name.title())