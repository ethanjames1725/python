"""Loops through a list of cars printing each in title case (BMW in
uppercase), then demonstrates case-insensitive string comparison
using lower()."""
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Ignoring case when checking for equality
print("\nChecking for equality:")
car = 'Audi'
print("car = Audi")
print(f"car == 'audi': {car == 'audi'}")

print(f"car.lower() == 'audi': {car.lower() == 'audi'}")
