"""Demonstrates tuples: stores box dimensions, loops through them,
then reassigns the tuple to new dimensions and loops again."""
dimensions = (200, 50)
# dimensions[0] = 250 #TypeError: 'tuple' object does not support item
# assignment
print(dimensions[0])
print(dimensions[1])
# Looping through tuples:
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
