"""Summary"""
from pathlib import Path

MESSAGE = "I really like dogs."
MESSAGE.replace('dog', 'cat')

print(MESSAGE)

path = Path(__file__).parent/'learning_python.txt'
contents = path.read_text()

for line in contents.splitlines():
    print(line.replace('Python', 'C'))
