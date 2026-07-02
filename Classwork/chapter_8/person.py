"""Demonstrate functions that return values by building dictionaries
of information about a person, with build_person_0() showing how an
optional age argument can be conditionally added to the result."""


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


def build_person_0(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person_0('jimi', 'hendrix', age=27)
print(musician)
