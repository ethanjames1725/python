"""summary"""
prompt = "Please enter your age to receive a movie ticket.\n"
prompt += "To exit, please enter 'quit'. "
active = True
price = 15

while active:
    user_input = input(prompt)
    if user_input == 'quit':
        break
    age = int(user_input)
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    print(f"The cost of your movie ticket is ${price}.")
    active = False
