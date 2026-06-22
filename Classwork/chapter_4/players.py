"""Demonstrates list slicing on a list of players, then loops
through a slice to print the first three players' names."""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
# last three players:
print(players[-3:])

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())
