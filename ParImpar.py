n = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))
m2 = 1
m = 1

if n%2 == 0 and n2%2 == 0 or n%2 == 1 and n2%2 == 1 :
    for i in range(2,n+1):
        r = n%i
        r2 = n2%i
        if r == 0 and r2 == 0:
            m = i
    print("Este es el maximo comun divisor: " , m)
elif n%2 == 0 and n2%2 == 1 or n%2 == 1 and n2%2 == 0:
    for i in range(2, max(n,n2)+1):
        if n%i == 0:
            n = n//i
            m2=m2*i
        elif n2%i == 0:
            n2 = n2//i
            m2=m2*i
    print("Este es el minimo comun multiplo: ", m2)
            