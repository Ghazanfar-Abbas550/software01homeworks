import random

# generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# first guess
guess = int(input("Guess the number (1–10): "))

# loop until guessed correctly
while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")
    guess = int(input("Guess the number (1–10): "))

print("You guessed correctly!")

# Output
# Guess the number (1–10): 2
# Too low! Try a higher number.
# Guess the number (1–10): 4
# Too high! Try a lower number.
# Guess the number (1–10): 3
# You guessed correctly!