"""Write a short multi-line message to programming.txt."""
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path(__file__).parent/'programming.txt'
path.write_text(contents)
