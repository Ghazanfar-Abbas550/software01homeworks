number = input("Enter number (press Enter to stop): ")
if number == "":
    print("No numbers entered.")
else:
    number = int(number)
    smallest = largest = number

    while True:
        number_input = input("Enter number (press Enter to stop): ")
        if number_input == "":
            break
        number = int(number_input)
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    print("Smallest number:", smallest)
    print("Largest number:", largest)