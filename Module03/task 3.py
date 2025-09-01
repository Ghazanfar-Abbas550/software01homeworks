Gender = input("Enter Gender (M/F): ")
hemoglobin_value = int(input("Enter hemoglobin value (g/l): "))
if Gender == "M" and hemoglobin_value >= 134 and hemoglobin_value <= 167:
    print("Hemoglobin value is normal")
elif Gender == "M" and hemoglobin_value < 134:
    print("Hemoglobin value is too low")
elif Gender == "M" and hemoglobin_value > 167:
    print("Hemoglobin value is too high")
elif Gender == "F" and hemoglobin_value >= 117 and hemoglobin_value <= 155:
    print("Hemoglobin value is normal")
elif Gender == "F" and hemoglobin_value < 117:
    print("Hemoglobin value is too low")
elif Gender == "F" and hemoglobin_value > 155:
    print("Hemoglobin value is too high")
else:
    print("Invalid input")


# Output
# Enter Gender (M/F): M
# Enter hemoglobin value (g/l): 138
# Hemoglobin value is normal