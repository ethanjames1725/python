"""Stores a glossary of Python terms and definitions and loops over
it to print each term formatted."""
glossary = {
    'tuple': 'an unchangable list',
    'dictionary': 'a collection of key-value pairs',
    'key': 'keys are connected to a value, and used to access the '
    'value associated with it',
    'list': 'a set of values',
    'conditional test': 'an expression that can be evaluated '
    'as true or false',
    'indentation': 'used to structure a program',
    'variable': 'a name that stores a value in memory',
    'function': 'a reusable block of code that performs a '
    'specific task',
    'loop': 'repeats a block of code multiple times',
    'string': 'a sequence of characters enclosed in quotes',
    'integer': 'a whole number without a decimal point'
}

for key, value in glossary.items():
    print(f"{key.title()}:\n\t{value}.\n")
