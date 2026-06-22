"""Builds a list of cubes (1-10) with a list comprehension, then
prints each cube on its own line."""
cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
    print(cube)
