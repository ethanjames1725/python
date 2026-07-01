"""
Creates a list of pets, removes all instances of 'cat' from the list,
and prints the modified list of pets.
"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
