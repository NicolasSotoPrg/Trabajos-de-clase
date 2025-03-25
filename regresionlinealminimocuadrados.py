import random as rnd
Y = []
X = []
n = 2
mp = 0
for i in range(n):
    X.append(rnd.randint(50, 200))
    Y.append(rnd.randint(40, 300))
print(X)
print(Y)
for x in X:
    x2 = x
    print(x2)
for y in Y:
    y2 = y
    print(y2)
    mp = x2 + y2
    print(mp)