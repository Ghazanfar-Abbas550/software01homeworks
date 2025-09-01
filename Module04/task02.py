inches = input("Enter value in inches (or 'stop' to quit): ")

while inches != 'stop':
    inches_float = float(inches)
    centimeters = inches_float * 2.54
    print(centimeters)
    inches = input("Enter value in inches (or 'stop' to quit): ")

# Output
# Enter value in inches (or 'stop' to quit): 2
# 5.08
# Enter value in inches (or 'stop' to quit): 4
# 10.16
# Enter value in inches (or 'stop' to quit): stop