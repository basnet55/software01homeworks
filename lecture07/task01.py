import  random

def dice():
   return random.randint(1, 6)

def roll_dice2():
    roll = 0
    while roll!=6:
        roll = dice()
        print(f"You have rolled; {roll}")

roll_dice2()