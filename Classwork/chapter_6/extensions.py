"""Extension of the favourite_places exercise: each person maps to a nested
dictionary of places with population, top attraction and a fun fact."""
favourite_places = {
    'adam': {
        'maldives': {
            'population': 521_021,
            'most popular attraction': 'Snorkelling and diving in coral reefs',
            'fun fact': 'The Maldives is the lowest-lying country in the '
            'world, with an average ground level of just 1.5 metres above '
            'sea level.',
        },
        'bali': {
            'population': 4_200_000,
            'most popular attraction': 'Tanah Lot Temple',
            'fun fact': 'Bali is known as the "Island of the Gods" and '
            'has more than 10,000 temples.',
        },
        'croatia': {
            'population': 3_900_000,
            'most popular attraction': 'Plitvice Lakes National Park',
            'fun fact': 'Croatia has 1,246 islands along its Adriatic '
            'coastline, though only about 50 are permanently inhabited.',
        },
    },

    'ana': {
        'greece': {
            'population': 10_400_000,
            'most popular attraction': 'The Acropolis of Athens',
            'fun fact': 'Greece has more archaeological museums than any '
            'other country in the world.',
        },
        'paris': {
            'population': 2_100_000,
            'most popular attraction': 'The Eiffel Tower',
            'fun fact': 'The Eiffel Tower grows about 15 cm taller in summer'
            ' due to the thermal expansion of iron.',
        },
        'cyprus': {
            'population': 1_260_000,
            'most popular attraction': 'Aphrodite Hills and the birthplace '
            'of Aphrodite at Petra tou Romiou',
            'fun fact': 'Cyprus is said to be the birthplace of Aphrodite, '
            'the Greek goddess of love and beauty.',
        },
    },

    'nathan': {
        'japan': {
            'population': 125_700_000,
            'most popular attraction': 'Mount Fuji',
            'fun fact': 'Japan has over 6,800 islands and is home to the '
            'world\'s oldest company, Kongo Gumi, a construction firm '
            'founded in 578 AD.',
        },
        'hawaii': {
            'population': 1_440_000,
            'most popular attraction': 'Waikiki Beach and Diamond Head Crater',
            'fun fact': 'Hawaii is the only US state that grows coffee '
            'commercially and is home to the world\'s most active volcano,'
            ' Kilauea.',
        },
        'rome': {
            'population': 2_800_000,
            'most popular attraction': 'The Colosseum',
            'fun fact': 'Rome has the highest concentration of historical '
            'sites in the world, and all roads in the ancient Roman Empire'
            ' literally led to Rome.',
        },
    },
}

for person, places in favourite_places.items():
    print(f"{person.title()}'s favourite places:")
    for place, info in places.items():
        print(f"\t{place.title()}:")
        for k, v in info.items():
            print(f"\t\t{k.title()}: {v}")
    print()
