year_input = int(input("Enter year: "))
if year_input % 4 == 0:
    print("Its a leap year")
elif year_input % 100 == 0 and year_input % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

# Output
# Enter year: 2025
# It is not a leap year