requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Checking whether a value is in a list:
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(f"\nRequested Toppings:{requested_toppings}\n")
print(f"'mushrooms' in requested_toppings: {'mushrooms' in requested_toppings}")
print(f"'pepperoni' in requested_toppings: {'pepperoni' in requested_toppings}")

print("\nMultiple if statement:\n")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")