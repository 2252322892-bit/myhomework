import math

while True:
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        if a == 0:
            print("a cannot be 0. Try again.")
            continue

        d = b**2 - 4*a*c

        if d < 0:
            print("The roots are not real. Try again.")
            continue

        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)

        print("Root 1 =", x1)
        print("Root 2 =", x2)
        break

    except:
        print("Invalid input. Try again.")