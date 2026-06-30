"""Summary"""
from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored username if available."""
    if path.exists() and path.read_text().strip():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def get_new_user_info(path):
    """Prompt for a new username."""
    username = input("What is your username? ")
    name = input("What is your name? ")
    age = input("What is your age? ")
    contents = {'username': username, 'name': name, 'age': age}
    path.write_text(json.dumps(contents))
    return contents


def remember_user(user_info):
    """Prints a summary of user info."""
    print("\nWe'll remember you when you come back!")
    print("What will be remembered:")
    print(f"\tUsername: {user_info['username']}")
    print(f"\tName: {user_info['name'].title()}")
    print(f"\tAge: {user_info['age']}")


def greet_user():
    """Greet the user by name."""
    path = Path(__file__).parent/'username.json'
    user_info = get_stored_user_info(path)
    if user_info:
        prompt = f"Is {user_info['username']} your correct username? (y/n) "
        user_confirm = input(prompt)
        if user_confirm.lower() == 'y':
            print(f"Welcome back, {user_info['username']}!")
            print(f"{user_info['username']}\n{user_info['name'].title()}"
                  f"\n{user_info['age']}")
        elif user_confirm.lower() == 'n':
            user_info = get_new_user_info(path)
            remember_user(user_info)
        else:
            print("Please enter 'y' for yes, or 'n' for no.")
    else:
        user_info = get_new_user_info(path)
        remember_user(user_info)


greet_user()
