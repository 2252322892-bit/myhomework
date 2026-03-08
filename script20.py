def f(x):
    return x**2 / 2

a = 0
b = 3
n = 6
dx = (b - a) / n

rect_area = 0
x = a

for i in range(n):
    rect_area = rect_area + f(x) * dx
    x = x + dx

true_area = (b**3 / 6) - (a**3 / 6)

print("Rectangle area =", rect_area)
print("True area =", true_area)
print("Difference =", true_area - rect_area)