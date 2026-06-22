"""Maps rivers to the countries they run through and prints sentences,
then just the keys, then just the values."""
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'orange': 'south africa',
}

print("Sentence:")
for key, val in rivers.items():
    print(f"The {key.title()} runs through {val.title()}.")

print("\nRiver:")
for key in rivers.keys():
    print(key.title())

print("\nCountry:")
for val in rivers.values():
    print(val.title())
