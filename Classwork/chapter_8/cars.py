"""Demonstrate the different ways to import and call make_car() from
the cars_functions module: import the module, import with an alias,
import a specific function (with and without an alias), and import
everything with *. Only the first style is active; the rest are
commented out to show the alternative syntax."""
import cars_functions

car = cars_functions.make_car('subaru', 'outback',
                              color='blue', tow_package=True)
print(car)


# import cars_functions as cf

# car = cf.make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)


# from cars_functions import make_car

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)


# from cars_functions import make_car as mc

# car = mc('subaru', 'outback', color='blue', tow_package=True)
# print(car)


# from cars_functions import *

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)
