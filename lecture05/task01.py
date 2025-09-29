import random
rolled_dice = int(input("How many dices do you want to roll?: "))

total = 0
for i in range(rolled_dice):
    roll = random.randint(1, 6)
    total=total+ roll
print("The sum of the dice is:", total)

