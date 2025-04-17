while True:
    n = int(input("Ingresa el tamaño de la matriz cuadrada: "))
    if n == 0:
        #Si se pone 0 se detiene el ciclo
        break

    matriz = []

    for i in range(n):
        fila = list(map(int, input("Ingresa los valores de la fila: ").split()))
        #input().split(). lee cada liea con los numeros separadas por espacios
        #map(int,) convierte el texto a numeros enteros y list() convierte ese resultado en una lista
        matriz.append(fila)

    superior = True
    inferior = True
    #La matriz es superior e inferios, si un valor esta fuera de lugar pasa a false

    # Verificar si es triangular superior o inferior
    for i in range(n):
        for j in range(n):
            if i > j and matriz[i][j] != 0:
                #Se analiza debajo de la diagonal, si hay un numero diferente a 0, no es triangular superior
                superior = False
            if i < j and matriz[i][j] != 0:
                #Se analiza arriba de la diagonal, si hay un numero diferente a 0, no es triangular inferior
                inferior = False

    if superior or inferior:
        print("SI")
    else:
        print("NO")
