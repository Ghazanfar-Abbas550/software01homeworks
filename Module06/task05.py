def remove_odds(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_list = remove_odds(my_list)

print("Original list:", my_list)
print("Even-only list:", filtered_list)


# Output
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Even-only list: [2, 4, 6, 8]