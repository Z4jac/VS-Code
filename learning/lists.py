"""
sq = []
for i in range(1, 101):
    sq.append(i**2)



sq2 = [i**2 for i in range(1, 101)]

print(sq2)
"""
########################################################
"""
remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)
"""
########################################################
"""
v = [2, -3, 1]
w = [4*x for x in v]
print(w)
"""

#######################################################

A = list(range(1, 101))
B = list(range(1, 101))

cartesian_product = [(a, b) for a in A for b in B if (a/b > a-b)]
print(cartesian_product)
print(f"liczba par: {len(cartesian_product)}")
