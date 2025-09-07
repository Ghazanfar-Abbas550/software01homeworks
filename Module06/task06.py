import math

# Function to calculate unit price per square meter
def unit_price(diameter_cm, price_euros):
    radius_m = (diameter_cm / 2) / 100  # convert cm to meters
    area = math.pi * (radius_m ** 2)
    return price_euros / area

# Main program
d1 = float(input("Enter diameter of pizza 1 (cm): "))
p1 = float(input("Enter price of pizza 1 (€): "))

d2 = float(input("Enter diameter of pizza 2 (cm): "))
p2 = float(input("Enter price of pizza 2 (€): "))

price1 = unit_price(d1, p1)
price2 = unit_price(d2, p2)

print(f"Pizza 1 unit price: {price1:.2f} €/m²")
print(f"Pizza 2 unit price: {price2:.2f} €/m²")

if price1 < price2:
    print("Pizza 1 is better value.")
else:
    print("Pizza 2 is better value.")


# Output
# Enter diameter of pizza 1 (cm): 30
# Enter price of pizza 1 (€): 10
# Enter diameter of pizza 2 (cm): 40
# Enter price of pizza 2 (€): 14
# Pizza 2 is better value (lower €/m²).