base = int(input("base? "))
power = int(input("power? "))

answer = 1
text = ""

for i in range(power):
    answer = answer * base
    text = text + str(base)
    if i < power - 1:
        text = text + "X"

print(text + "=" + str(answer))