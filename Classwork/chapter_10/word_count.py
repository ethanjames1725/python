"""Summary"""
from pathlib import Path


def count_words(file_path):
    """Count the approximate number of words in a file."""
    try:
        contents = file_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # pass
        print(f"Sorry, the file {file_path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_path} has about {num_words} words.")


file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
              'little_women.txt']
for file_name in file_names:
    path = Path(__file__).parent/file_name
    count_words(path)
