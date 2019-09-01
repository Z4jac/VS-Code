import re

n = list(open("liczby.txt", "r"))
m = []
'''
#print(n)
for i in n:
    #Usuwanie \n i zmiana STRING na INT
    g = i.strip("\n")
    m.append(int(g))


w = []
for i in m:
    while (i%3 == 0):
       i = i / 3
    return i == 1
    if True:
       w.append(i)

print(len(w))
'''

liczby = re.compile(r'\d+')
for i in n:
    m.append(int(liczby.findall(i)))
print(m)
