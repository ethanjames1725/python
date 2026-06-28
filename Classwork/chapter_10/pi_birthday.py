"""Summary"""
from pathlib import Path

path = Path(__file__).parent / 'pi_million_digits.txt'
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.strip()

birthday = input("Please enter your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    print(f"Your birthday appears after the {pi_string.index(birthday)} "
          "digit.")
else:
    print("Your birthday appears somewhere after the first "
          "million digits of pi!")
