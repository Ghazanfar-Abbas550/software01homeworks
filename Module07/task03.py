airport_dict = {}
start = input("Choose an option: (1 = enter new airport, 2 = fetch airport, 3 = quit): ")

while start != "3":
    if start == "1":
        ICAO = input("Enter ICAO code: ")
        Airport = input("Enter Airport name: ")
        airport_dict[ICAO] = Airport
    if start == "2":
        ICAO = input("Enter ICAO code: ")
        find_airport = airport_dict.get(ICAO)
        if find_airport != None:
            print(find_airport)
        else:
            print("No airport found. ")
    start = input("Choose an option: (1 = enter new airport, 2 = fetch airport, 3 = quit): ")


# Output
# Choose an option: (1 = enter new airport, 2 = fetch airport, 3 = quit): 2
# Enter ICAO code: EFHK
# No airport found.
#
# Choose an option: (1 = enter new airport, 2 = fetch airport, 3 = quit): 1
# Enter ICAO code: EFHK
# Enter Airport name: Helsinki-Vantaa Airport
#
# Choose an option: (1 = enter new airport, 2 = fetch airport, 3 = quit): 2
# Enter ICAO code: EFHK
# Helsinki-Vantaa Airport
#
# Choose an option: (1 = enter new airport, 2 = fetch airport, 3 = quit): 3
#