season = ("spring", "summer", "autumn", "winter")

month = int(input("Enter a number of month: "))
if month in (12, 1, 2):
    print(season[3])
elif month in (3,4,5):
    print(season[0])
elif month in (6,7,8):
    print(season[1])
elif month in (9,10,11):
    print(season[2])

# Output
# Enter a number of month: 9
# autumn