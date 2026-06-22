"""Builds a list of numbers 1-20 three ways: a list comprehension, an
empty list filled in a loop, and a plain range() printed directly."""
counting = [value for value in range(1, 21)]
print(counting)
values = []
for value in range(1, 21):
    values.append(value)
print(values)
for value in range(1, 21):
    print(value)
