import random

N = int(input("Enter how many random points to generate: "))

n = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        n += 1

pi_approx = 4 * n / N

print("Approximation of pi:", pi_approx)

# Output
# Enter how many random points to generate: 2
# Approximation of pi: 4.0
