#4.1
file = open("sygnaly.txt")

for i, line in enumerate(file):
    line = line.strip()
    if (i + 1) % 40 == 0:
        print(line[9], end = "")
