"""Nested dictionary of cities, each holding country, population and fun-fact
data, looped over to print a formatted profile per city."""
cities = {
    'johannesburg': {
        'country': 'south africa',
        'population': 12_000_000,
        'fact': 'Johannesburg is the world\'s largest urban forest, home to '
        'over 10 million trees',
    },

    'tokyo': {
        'country': 'japan',
        'population': 14_270_000,
        'fact': 'Tokyo is home to the world\'s busiest pedestrian crossing, '
        'Shibuya Crossing, where up to 3000 people cross at the exact same '
        'time during peak hours',
    },

    'cairo': {
        'country': 'egypt',
        'population': 22_600_000,
        'fact': 'Cairo is home to the world\'s oldest surviving university, '
        'Al-Alzhar University, which was founded in 970 AD and still operates '
        'today',
    },

}

for city, cities_info in cities.items():
    print(f"City: {city.title()}")
    for info_k, info_v in cities_info.items():
        value = str(info_v).title() if info_k == 'country' else info_v
        print(f"\t{info_k.title()}: {value}")
    print()
