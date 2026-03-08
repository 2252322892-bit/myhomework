n = 1
total = 0

while True:
    term = 1 / (n ** 2)
    if term < 0.000001:
        break
    total = total + term
    n = n + 1

print("Sum =", total)