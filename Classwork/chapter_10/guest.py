"""Prompt the user for their name and save it to guest.txt."""
from pathlib import Path

guest_info = input("Please enter your name. ")

path = Path(__file__).parent/'guest.txt'
path.write_text(guest_info.title())
