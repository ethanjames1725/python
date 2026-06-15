favourite_places = {
    'adam': ['croatia', 'bali', 'maldives'],
    'ana': ['greece', 'paris', 'cyprus'],
    'nathan': ['japan', 'hawaii', 'rome'],
}

for name, places in favourite_places.items():
    print(f"Name: {name.title()}\nFavourite Places: ")
    for place in places:
        print(f"\t{place.title()}")
    print()