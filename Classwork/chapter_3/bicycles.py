"""Summary: This code creates a list of bicycles and prints out the names of
the bicycles in a title format, including the first, second, third, fourth,
and last bicycle owned, using indexing to access the elements of the list."""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)
print(f"The first bicycle I owned was a {bicycles[0].title()}.")
print(f"The second bicycle I owned was a {bicycles[1].title()}.")
print(f"The third bicycle I owned was a {bicycles[2].title()}.")
print(f"The fourth bicycle I owned was a {bicycles[3].title()}.")
print(f"The last bicycle I owned was a {bicycles[-1].title()}.")
