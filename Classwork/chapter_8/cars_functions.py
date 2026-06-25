"""Summary"""


def make_car(manufacturer, car_name, **car_info):
    """Stores information about a car in a dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['car_name'] = car_name
    return car_info
