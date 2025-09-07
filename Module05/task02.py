num_list = []

num = input("Enter number or press ENTER to exit: ")
while num != "":
    num_list.append(int(num))
    num = input("Enter number or press ENTER to exit: ")

num_list.sort(reverse=True)
print(num_list[:5])

# Output
# Enter number or press ENTER to exit: 12
# Enter number or press ENTER to exit: 13
# Enter number or press ENTER to exit: 25
# Enter number or press ENTER to exit: 9
# Enter number or press ENTER to exit: 89
# Enter number or press ENTER to exit: 7
# Enter number or press ENTER to exit: 34
# Enter number or press ENTER to exit: 67
# Enter number or press ENTER to exit:
# [89, 67, 34, 25, 13]
