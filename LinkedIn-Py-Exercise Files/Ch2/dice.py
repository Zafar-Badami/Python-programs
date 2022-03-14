import random
class Dice:
    def roll(self):
        roll1=random.randint(1,6)
        roll2=random.randint(1,6)
        return (roll1, roll2)

dice=Dice()
print(dice.roll())