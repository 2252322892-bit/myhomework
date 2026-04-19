import os

filename = "times_tables.txt"

if os.path.exists(filename):
    print("The file already exists. Program will quit.")
else:
    file = open(filename, "w")

    for i in range(1, 13):
        file.write("The " + str(i) + " times table:\n")

        for j in range(1, 13):
            file.write(str(i) + " x " + str(j) + " = " + str(i * j) + "\n")

        file.write("\n")

    file.close()
    print("Times tables have been written to the file.")