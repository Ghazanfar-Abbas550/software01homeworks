import random

def roll_dice(sides):
    return random.randint(1, sides)

# Main program
sides = int(input("Enter the number of sides on the dice: "))
roll = 0
while roll != sides:
    roll = roll_dice(sides)
    print(f"Roll: {roll}")

# Output
# Enter the number of sides on the dice: 6
# Roll: 4
# Roll: 4
# Roll: 1
# Roll: 1
# Roll: 5
# Roll: 1
# Roll: 3
# Roll: 1
# Roll: 5
# Roll: 2
# Roll: 3
# Roll: 5
# Roll: 4
# Roll: 6