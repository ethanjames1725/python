"""Summary"""
from pathlib import Path
import json

path = Path(__file__).parent/'favourite_number.json'

if path.exists() and path.read_text().strip():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"I know your favourite number! It's {fav_num}")
else:
    fav_num = input("Please enter your favourite number: ")
    contents = json.dumps(fav_num)
    path.write_text(contents)
    print(f"We will remember your favourite number! {fav_num}!")
