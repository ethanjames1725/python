"""Summary"""
import pytest
from employee import Employee


@pytest.fixture
def employee():
    """An employee that will be available for all test functions."""
    employee_0 = Employee('Ethan', 'Smith', 10000)
    return employee_0


def test_give_default_raise(employee):
    """Tests if default raise works."""
    employee.give_raise()
    assert employee.salary == 15000


def test_give_custom_raise(employee):
    """Tests if custom raise works."""
    employee.give_raise(1000)
    assert employee.salary == 11000
