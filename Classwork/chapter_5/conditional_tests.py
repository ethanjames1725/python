"""Tests equality and numerical comparison operators across several
variables, then combines conditions on pairs of ages using 'and'
and 'or'."""
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

bike = 'ducatti'
print("\nIs bike == 'yamaha'? I predict False.")
print(bike == 'yamaha')
print("Is bike == 'ducatti'? I predict True.")
print(bike == 'ducatti')

animal = 'falcon'
print("\nIs animal == 'falcon'? I predict True.")
print(animal == 'falcon')
print("Is animal == 'Falcon'? I predict False.")
print(animal == 'Falcon')

bicycle = 'Trek'
print("\nIs bicycle == 'trek.title()'? I predict True.")
print(bicycle == bicycle.title())
print("Is bicycle == 'trek.lower()'? I predict False.")
print(bicycle == bicycle.lower())
