import math

n = list(open("pogoda.txt", "r"))
m = []
w = []
c = []
for i in n:
    #Usuwanie \n
    g = i.strip("\n")
    m.append(g)
for i in m:
    d = i.split(sep=";")

    if len(d) > 3:
        d[1] = float(d[1].replace(',', '.'))
        d[2] = float(d[2].replace(',', '.'))

        if d[1] >= 20 and d[2] <=5:
            w.append(i)

print(len(w))
