"""Summary"""
from pathlib import Path

path = Path(__file__).parent / 'pi_million_digits.txt'
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:10]}...")
print(len(pi_string))
