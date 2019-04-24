#4.1
file = open("sygnaly.txt")

for i, line in enumerate(file):
    line = line.strip()
    print(line)
