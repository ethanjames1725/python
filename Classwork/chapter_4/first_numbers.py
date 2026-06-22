"""Demonstrates range() with different start and stop values, then
converts a range into a list and prints it."""
print("range 1-5:")
for value in range(1, 5):
    print(value)
print("\nrange 1-6:")
for value in range(1, 6):
    print(value)
number = list(range(1, 6))
print("\nnumber list:\n", number)
