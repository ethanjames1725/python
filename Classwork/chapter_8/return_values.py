"""Summary"""


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


def greet_person():
    """Greets the user"""
    while True:
        first_name = input("Enter a first name (or 'q' to quit): ").lower()
        if first_name == 'q':
            break

        last_name = input("Enter last name (or 'q' to quit): ").lower()
        if last_name == 'q':
            break

        age = input("Enter age (optional): ")
        if age == '':
            age = None
        else:
            age = int(age)

        person = build_person(first_name, last_name, age)

        print(f"Hello, {person['first'].title()} {person['last'].title()}!")

        if age:
            print(f"Age: {person['age']}")


greet_person()
