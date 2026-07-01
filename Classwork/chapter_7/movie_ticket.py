"""
Uses a while loop to prompt the user for their age and determine the cost
of a movie ticket based on their age. The loop continues until a valid age is
entered, and the final ticket price is printed.
"""
price = 15

while True:
    age = int(input("Please enter your age to receive a movie ticket. "))
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    break
print(f"The cost of your movie ticket is ${price}")
