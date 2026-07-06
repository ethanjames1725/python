"""Summary"""


def city_country(city, country, population=''):
    """Generate neatly formatted city, country, population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}."
    else:
        return f"{city.title()}, {country.title()}."
