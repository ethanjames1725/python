"""Summary"""


def describe_city(city_name, city_country='south africa'):
    """Display info about a city."""
    print(f"\n{city_name.title()} is in {city_country.title()}.")


describe_city('cape town')
describe_city('johannesburg')
describe_city('london', city_country='england')
