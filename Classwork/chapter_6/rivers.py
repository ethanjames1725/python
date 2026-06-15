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
