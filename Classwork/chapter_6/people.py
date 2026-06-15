person_0 = {
    'first name': 'john',
    'last name': 'smith',
    'age': 42,
    'city': 'new york',
}

person_1 = {
    'first name': 'anya',
    'last name': 'frey',
    'age': 34,
    'city': 'london',
}

person_2 = {
    'first name': 'michael',
    'last name': 'jackson',
    'age': 50,
    'city': 'gary',
}

people = [person_0, person_1, person_2]

for person in people:
    name = f"{person['first name']} {person['last name']}"
    print(f"Name: {name.title()}\nAge: {person['age']}\nCity: "
          "{person['city'].title()}\n")
