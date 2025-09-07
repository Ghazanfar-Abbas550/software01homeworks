import random

def roll_dice():
    return random.randint(1, 6)

roll = 0
while roll != 6:
    roll = roll_dice()
    print(f"Roll: {roll}")

# Output
# Roll: 3
# Roll: 5
# Roll: 6