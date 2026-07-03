"""Read and print the contents of cats.txt and dogs.txt.

Silently does nothing if either file is missing.
"""
from pathlib import Path

try:
    cat_path = Path(__file__).parent/'cats.txt'
    dog_path = Path(__file__).parent/'dogs.txt'
    cat_names = cat_path.read_text()
    dog_names = dog_path.read_text()

except FileNotFoundError:
    pass

else:
    print(cat_names)
    print(dog_names)
