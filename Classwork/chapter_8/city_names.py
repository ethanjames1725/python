"""summary"""


def city_country(c_name, c_country):
    """Returns a formatted string of a city and its country."""
    full_city = f"{c_name}, {c_country}"
    return full_city.title()


print(city_country('johannesburg', 'south africa'))
print(city_country('london', 'england'))
print(city_country('sydney', 'australia'))
