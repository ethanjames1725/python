"""summary"""
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Full name with 3 arguments:
def get_formatted_name_1(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_1('john', 'lee', 'hooker')
print(musician)

# Full name with an optional middle name argument
def get_formatted_name_2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_2('jimi', 'hendrix')
print(musician)

musician = get_formatted_name_2('john', 'hooker', 'lee')
print(musician)
