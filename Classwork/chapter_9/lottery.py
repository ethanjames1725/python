"""Summary"""
from random import choice

lottery_numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                   'a', 'b', 'c', 'd', 'e')
winning_ticket = []

while len(winning_ticket) < 4:
    rand_pick = choice(lottery_numbers)
    if rand_pick not in winning_ticket:
        winning_ticket.append(rand_pick)

print("Any ticket matching these 4 characters wins a prize:"
      f"\n\t{', '.join(winning_ticket)}")

my_ticket = []
num_draws = 0

while my_ticket != winning_ticket:
    num_draws += 1
    my_ticket = []
    while len(my_ticket) < 4:
        new_pick = choice(lottery_numbers)
        my_ticket.append(new_pick)

print(f"\nThe winning ticket was: {', '.join(my_ticket)}.")
print(f"It took {num_draws} draws to win.")
