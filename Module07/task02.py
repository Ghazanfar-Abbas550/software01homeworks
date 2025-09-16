names = set()
names_input = input("Enter name (or just Enter to quit):")
while names_input != "":
    if names_input in names:
        print("Existing name")
    else:
        print("New name")
        names.add(names_input)
    names_input = input("Enter name (or just Enter to quit): ")

for name in names:
    print(name)

# Output
# Enter name (or just Enter to quit): Alice
# New name
# Enter name (or just Enter to quit): Bob
# New name
# Enter name (or just Enter to quit): Alice
# Existing name
# Enter name (or just Enter to quit):
# Alice
# Bob