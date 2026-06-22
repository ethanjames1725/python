"""Copies a list of favourite pizzas, appends a different pizza to
each list, then prints both lists."""
pizzas = ["margherita", "nutella", "meat-lovers", "veggie", "bbq chicken"]
friends_pizza = pizzas[:]
pizzas.append("hawaiian")
friends_pizza.append("cheese")
print("My favourite pizzas are:")
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("\nMy friend's favourite pizzas are:")
for pizza in friends_pizza:
    print(f"My friend likes {pizza} pizza")
print("\nI really love pizza!")
