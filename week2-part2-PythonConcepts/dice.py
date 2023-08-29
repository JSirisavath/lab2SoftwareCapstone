import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


# myDice = Dice(14)

# for die in range(100):
#     print(myDice.roll())


# Default dice is 6
dice2 = Dice()

print(dice2.roll())
