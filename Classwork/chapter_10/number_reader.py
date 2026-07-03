"""Read a list of numbers from numbers.json and print it."""
from pathlib import Path
import json

path = Path(__file__).parent/'numbers.json'
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
