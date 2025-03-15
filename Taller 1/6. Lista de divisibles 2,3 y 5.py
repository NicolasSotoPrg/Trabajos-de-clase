n = int(input("Ingrese un numero: "))

for i in range(n+1):
    if i%2 == 0 and i%3 == 0 and i%5 == 0:
        print(i,"Divisible por 2,3 y 5")
    elif i%2 == 0 and i%5 == 0:
        print(i,"Divisible por 2 y 5")
    elif i%2 == 0 and i%3 == 0:
        print(i,"Divisible por 2 y 3")
    elif i%3 == 0 and i%5 == 0:
        print(i,"Divisible por 3 y 5")
    elif i%2 == 0:
        print(i,"Divisible por 2")
    elif i%3 == 0:
        print(i,"Divisible por 3")
    elif i%5 == 0:
        print(i,"Divisible por 5")
    else:
        print(i,"No es divisible por ninguno")
