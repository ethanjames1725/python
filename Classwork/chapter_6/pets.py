pet_0 = {
    'pet name': 'chloe',
    'animal': 'cat',
    'age': '7',
    'owner name': 'daniel',
}

pet_1 = {
    'pet name': 'keira',
    'animal': 'cat',
    'age': '6',
    'owner name': 'adam',
}

pet_2 = {
    'pet name': 'bella',
    'animal': 'dog',
    'age': '8',
    'owner name': 'riley',
}

pet_3 = {
    'pet name': 'chicken',
    'animal': 'parrot',
    'age': '15',
    'owner name': 'sophie',
}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
    for key, val in pet.items():
        print(f"{key.title()}: {val.title()}")
    print()