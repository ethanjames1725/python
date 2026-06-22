"""Loops through a list of magicians to print their names, then loops
again to print a personalized trick message for each magician."""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print()
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
