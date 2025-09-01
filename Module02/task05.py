talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter ots: "))
total_lots = ((talents*20)+pounds)*32+lots
total_grams = total_lots*13.3
kilograms = total_grams//1000
remaining_grams = total_grams%1000
print("The weight in modern units: ")
print(f'{kilograms} kilograms and {remaining_grams:.2f} grams')

#Output
#Enter talents: 3
#Enter pounds: 9
#Enter ots: 13.5
#The weight in modern units: 
#29.0 kilograms and 545.95 grams
