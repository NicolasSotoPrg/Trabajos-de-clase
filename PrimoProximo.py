n = int(input("Ingresa un numero: "))

for n1 in range(2, n+1):
    dv = 0
    i = 2
    while i < n1 :
        if n1 % i == 0 :
            dv = dv + 1
        i = i + 1
    if dv <= 0 :
        pr = n1
print("el numero primo mas cercano es:",pr)
