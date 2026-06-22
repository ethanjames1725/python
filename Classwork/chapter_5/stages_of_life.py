"""Uses an if/elif/else chain to classify a person's stage of life
(baby, toddler, kid, teenager, adult, or elder) based on their
age."""
age = 200

if age < 2 and age >= 0:
    print("The person is a baby!")
elif age >= 2 and age < 4:
    print("The person is a toddler!")
elif age >= 4 and age < 13:
    print("The person is a kid!")
elif age >= 13 and age < 20:
    print("The person is a teenager!")
elif age >= 20 and age < 65:
    print("The person is an adult!")
elif age >= 65 and age <= 122:
    print("The person is an elder!")
else:
    print("This is the oldest person on Earth!!!")
