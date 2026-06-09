# This program demonstrates how to loop through a list of magicians and print their names, 
# as well as a personalized message for each magician.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
        print(magician)
print()
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")