# Detailed Summary: This code snippet demonstrates the use of various built-in functions in Python to manipulate a list of countries. 
# It shows how to find the number of items in the list using `len()`, sort the list in both alphabetical and 
# reverse alphabetical order using `sorted()` and `reverse()`, remove items from the list using `pop()` and `remove()`, 
# and add new items using `insert()` and `append()`. The code also uses the `del` statement to remove an item by index. 
# Each operation is followed by a print statement to display the results.
# This program demonstrates the use of the built-in functions in Python that have been covered in this chapter.

countries = ["South Africa", "Australia", "Canada", "Brazil", "Argentina", "Zimbabwe", "Mauritius"]

# Using the len() function to find the number of countries in the list
number_of_countries = len(countries)
print("Number of countries in the list:", number_of_countries)

# Using the sorted() and reverse() functions to sort the list of countries in alphabetical order
sorted_countries = sorted(countries)
print("Sorted list of countries:", sorted_countries)
sorted_countries.reverse()
print("Countries in reverse alphabetical order:", sorted_countries)

# Using the pop() function to remove the last country from the list
last_country = countries.pop()
print("Removed the last country from the list:", last_country)
print("Updated list of countries:", countries)

# Using the insert() function to add a new country to the list at a specific index
countries.insert(2, "New Zealand")
print("Added New Zealand to the list at index 2:", countries)

# Using the append() function to add a new country to the end of the list
countries.append("India")
print("Added India to the end of the list:", countries)

# Using the del statement to remove a country from the list by index
del countries[3]
print("Updated list of countries:", countries)

# Using the remove() function to remove a country from the list by value
countries.remove("Australia")
print("Removed Australia from the list:", countries)
