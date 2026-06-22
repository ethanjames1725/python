"""Builds a list of square numbers (1-10) with a for loop and
append(), then prints the range and the squares."""
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(list(range(1, 11)))
print(squares)
