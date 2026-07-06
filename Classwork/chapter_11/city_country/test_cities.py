"""Tests for the city_country function, with and without population."""
from city_functions import city_country


def test_city_country():
    """Does 'santiago, chile' work?"""
    city_country_0 = city_country('santiago', 'chile')
    assert city_country_0 == 'Santiago, Chile.'


def test_city_country_population():
    "Does 'santiago, chile 5_000_000' work?"
    city_country_pop = city_country('santiago', 'chile', 5_000_000)
    assert city_country_pop == 'Santiago, Chile - population 5000000.'
