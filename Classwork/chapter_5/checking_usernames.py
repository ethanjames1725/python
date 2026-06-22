"""Checks a list of new usernames against existing users
case-insensitively to determine whether each is already taken or
still available."""
current_users = ['ethan', 'james', 'smith', 'Abby', 'corio']
current_users_lower = [user.lower() for user in current_users]
new_users = ['Ethan', 'michael', 'albert', 'jack', 'abby']

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} has already been used. Please choose another.")
    else:
        print(f"The username: {user} is available.")
