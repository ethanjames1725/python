"""Load a stored username from username.json and greet that user."""
from pathlib import Path
import json

path = Path(__file__).parent/'username.json'
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")
