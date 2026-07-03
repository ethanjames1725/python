"""Read alice.txt and report its approximate word count.

Prints an error message instead if the file cannot be found.
"""
from pathlib import Path

path = Path(__file__).parent/'alice.txt'
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
