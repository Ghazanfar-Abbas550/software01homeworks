import random
rolls_list = []

rolls = int(input("Enter how many times to roll dice: "))
while rolls > 0:
    rolls_list.append(random.randint(1,6))
    rolls = rolls - 1

rolls_total = sum(rolls_list)
print(rolls_total)

# Output
# Enter how many times to roll dice: 2
# [2, 6]
# 8