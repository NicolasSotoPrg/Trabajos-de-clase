n1 = int(input())
n2 = int(input())
if n1 > n2:
    for i in range(n1 * n2, n1 - 1, -1):
        if i % n1 == 0 and i % n2 == 0:
            mcm = i
else:
    if n1 < n2:
        for i in range(n1 * n2, n2 - 1, -1):
            if i % n1 == 0 and i % n2 == 0:
                mcm = i
    else:
        mcm = n2
print(mcm)
