"""Write a hard-coded list of numbers to numbers.json."""
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path(__file__).parent/'numbers.json'
contents = json.dumps(numbers)
path.write_text(contents)
