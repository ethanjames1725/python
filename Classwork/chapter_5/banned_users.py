"""Checks whether a user is in a list of banned users and prints a
message allowing them to post if they are not banned."""
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
