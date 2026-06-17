"""summary"""
sandwich_orders = ['ham', 'pastrami', 'tuna', 'egg mayo', 'pastrami', 'tomato',
                   'nutella', 'pastrami']
finished_sandwiches = []

print("We regret to inform you that we have, "
      "sadly, run out of fresh pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich.title()} sandwich!")
    finished_sandwiches.append(sandwich)

print("\nCompleted Orders:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} sandwich")
