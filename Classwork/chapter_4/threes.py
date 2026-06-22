"""Builds and prints a list of multiples of three from 3 to 30
using a list comprehension."""
threes = [value for value in range(3, 31, 3)]
for three in threes:
    print(three)
