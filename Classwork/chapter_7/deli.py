"""summary"""
sandwich_orders = ['ham', 'tuna', 'egg mayo', 'tomato', 'nutella']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich.title()} sandwich!")
    finished_sandwiches.append(sandwich)

print("\nCompleted Orders:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} sandwich")
