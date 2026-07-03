"""Read pi_digits.txt and print its contents one line at a time."""
from pathlib import Path

path = Path(__file__).parent/'pi_digits.txt'
contents = path.read_text()

for line in contents.splitlines():
    print(line)
