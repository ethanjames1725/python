"""Loops through a list of feline animals printing a caution message,
then demonstrates list slicing: first three, middle three, and last
three items."""
animals = ["cheetah", "lion", "tiger", "leopard", "jaguar"]
for animal in animals:
    print(f"A {animal.title()} would probably not make a great pet.")
print("\nAny of these feline animals would be a great sighting in the wild!")

# Slices:
print("The first three items in the list are:")
print(animals[:3])
print("Three items from the middle of the list:")
print(animals[1:4])
print("The last three items in the list are:")
print(animals[-3:])
