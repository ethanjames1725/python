"""A class that simulates rolling dice with a configurable number of sides."""
from random import randint


class Dice:
    """Represents a die that can be rolled to produce random numbers."""

    def __init__(self, sides=6):
        """Initialises Dice attributes."""
        self.sides = sides

    def roll_die(self, number_of_rolls):
        """
        Prints a random number between 1 and number of sides the die has.
        """
        print(f"\nNow rolling the {self.sides}-sided die {number_of_rolls}"
              " times:")
        for roll in range(1, number_of_rolls + 1):
            print(f"\tRoll {roll}: {randint(1, self.sides)}")


dice_6 = Dice()
dice_6.roll_die(10)

dice_10 = Dice(sides=10)
dice_10.roll_die(10)

dice_20 = Dice(sides=20)
dice_20.roll_die(10)
