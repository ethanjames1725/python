"""Build a personal profile dictionary using build_profile()'s
**user_info to collect an arbitrary number of keyword arguments."""


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile('ethan', 'smith', location='johannesburg',
                           field='information technology', age=21)
print(my_profile)
