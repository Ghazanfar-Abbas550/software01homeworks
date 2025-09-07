def gallons_to_liters(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input("Enter gallons (negative to quit): "))
    if gallons < 0:
        print("Exiting...")
        break
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons = {liters} liters")

# Output
# Enter gallons (negative to quit): 10
# 10.0 gallons = 37.8541 liters
# Enter gallons (negative to quit): 3
# 3.0 gallons = 11.35623 liters
# Enter gallons (negative to quit): 2
# 2.0 gallons = 7.57082 liters
# Enter gallons (negative to quit): -3
# Exiting...
