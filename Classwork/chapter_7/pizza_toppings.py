"""summary"""
toppings = []
prompt = "Please enter the pizza toppings you wish to add.\n"
prompt += "When you are finished, please enter 'quit' to finalise your order. "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"\nWe will add {topping} to your pizza!\n")
        toppings.append(topping)
        continue
    break
if len(toppings) > 1:
    print(f"\nYour pizza with {', '.join(toppings[:-1])}, and {toppings[-1]} "
          "is ready!")
elif len(toppings) == 1:
    print(f"\nYour pizza with {toppings[0]} is ready!")
else:
    print("\nYour pizza with no toppings is ready!")
