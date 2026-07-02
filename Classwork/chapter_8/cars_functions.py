"""Module defining make_car(), which stores a car's manufacturer and
model along with an arbitrary number of extra keyword attributes
(**car_info) in a dictionary. Meant to be imported by cars.py."""


def make_car(manufacturer, car_name, **car_info):
    """Stores information about a car in a dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['car_name'] = car_name
    return car_info
