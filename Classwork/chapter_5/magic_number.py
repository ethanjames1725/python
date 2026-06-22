"""Demonstrates numerical comparison operators, then combines
conditions with 'and' and 'or' across pairs of age variables."""
# Numerical Comparisons
age = 18
print("age = 18")
print(f"age == 18: {age == 18}\n")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print("\nage = 19\n")
print(f"age < 21: {age < 21}")
print(f"age <= 21: {age <= 21}")
print(f"age > 21: {age > 21}")
print(f"age >= 21: {age >= 21}")

# Using AND
age_0 = 22
age_1 = 18
print("\nage_0 = 22\nage_1 = 18\n")
print(f"age_0 >= 21 and age_1 >= 21: {age_0 >= 21 or age_1 >= 21}")
print("\nage_0 = 22\nage_1 = 22\n")
age_1 = 22
print(f"age_0 >= 21 and age_1 >= 21: {age_0 >= 21 or age_1 >= 21}")

# Using OR
age_1 = 18
print("\nUsing OR")
print("\nage_0 = 22\nage_1 = 18\n")
print(f"age_0 >= 21 or age_1 >= 21: {age_0 >= 21 or age_1 >= 21}")
print("\nage_0 = 18\nage_1 = 22\n")
age_0 = 18
print(f"age_0 >= 18 or age_1 >= 21: {age_0 >= 21 or age_1 >= 21}")
