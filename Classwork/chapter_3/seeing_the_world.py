"""Detailed Summary: This code snippet demonstrates how to manipulate a list of
locations using various list methods in Python.
It starts by creating a list of locations and printing the original list.
Then, it uses the `sorted()` function to display a sorted version of the list
without modifying the original list.
Next, it reverses the order of the original list using the `reverse()` method
and prints the modified list.
It then reverses the list again to restore the original order. Finally,
it sorts the list in ascending order using the `sort()` method and then
in descending order by passing `reverse=True` to the `sort()` method, printing
the results after each operation."""

# define the original list
locations = ['Paris', 'New York', 'Tokyo', 'Sydney', 'Cairo']
print(f"Original list of locations: {locations}")

# sorted() returns a new sorted list, leaving the original unchanged
print(f"\nSorted list of locations: {sorted(locations)}")
# confirms original is unmodified
print(f"\nOriginal list of locations after sorted(): {locations}")

locations.reverse()  # reverses the list in place
print(f"\nList of locations after reverse(): {locations}")

locations.reverse()  # reverses again to restore original order
print(f"\nList of locations after reversing again: {locations}")

locations.sort()  # sorts the list in place alphabetically (ascending)
print(f"\nList of locations after sort(): {locations}")

# sorts in place in descending (reverse alphabetical) order
locations.sort(reverse=True)
print(f"\nList of locations after sort(reverse=True): {locations}")
