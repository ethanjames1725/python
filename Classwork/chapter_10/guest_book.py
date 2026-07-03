"""Repeatedly prompt for visitor names and log them to guest_book.txt.

Appends each entered name to the guest book until the user enters
'q' to quit.
"""
from pathlib import Path

path = Path(__file__).parent/'guest_book.txt'
guest_info = ''

while True:
    guest_input = input("Please enter your name.\n(quit with 'q') ")

    if guest_input.lower() == 'q':
        break

    guest_info += f"{guest_input}\n"

path.write_text(guest_info.title())
