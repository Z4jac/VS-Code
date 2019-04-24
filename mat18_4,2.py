file = open("przyklad.txt")

M = 0
for i,line in enumerate(file):
    f = line.strip()
    if M < len(set(f)):
        M = len(set(f))
        ten = f
        ile = len(set(f))
print(ten, ile)
