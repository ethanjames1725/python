"""Summary"""
from pathlib import Path

path = Path(__file__).parent/'guest_book.txt'
guest_info = ''

while True:
    guest_input = input("Please enter your name.\n(quit with 'q') ")

    if guest_input.lower() == 'q':
        break

    guest_info += f"{guest_input}\n"

path.write_text(guest_info.title())
