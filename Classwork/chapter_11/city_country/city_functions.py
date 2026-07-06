"""
Provides a function that formats a city, country, and optional population.
"""


def city_country(city, country, population=''):
    """Generate neatly formatted city, country, population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}."
    else:
        return f"{city.title()}, {country.title()}."
