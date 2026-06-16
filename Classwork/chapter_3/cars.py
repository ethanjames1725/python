"""Summary: This code demonstrates how to sort a list of cars in both ascending
and descending order, as well as how to reverse the order of the list.
It also shows how to use the sorted() function to display a sorted version of
the list without modifying the original list.
Finally, it prints out the number of cars in the list using the len() function.
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n\nHere is the original list:")
print(cars)
cars.reverse()
print("\nHere is the reversed list:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\nI have {len(cars)} cars in my list.")
