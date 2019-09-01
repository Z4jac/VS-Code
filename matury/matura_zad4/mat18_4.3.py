#4.3
file = open("przyklad.txt")

for i,line in enumerate(file):
    f = line.strip()
    l = sorted(list(f))
    if ord(l[-1]) - ord(l[0]) <=10:
        print(f)
