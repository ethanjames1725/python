"""Checks a list of people against a favourite-languages dictionary and
prints a thank-you or a reminder to take the poll."""
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'matt': 'java',
    'joel': 'javascript',
}

people = ['matt', 'joel', 'ethan', 'james']

for name in people:
    if name in favourite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll!")
    else:
        print(f"{name.title()}, please take the poll!")
