print("Ingresa los numeros a promediar, para dar el resultado ingresa 0")
suma = 0
divisor = 0
promedio = 0
suma2 = 0
divisor2 = 0
promedio2 = 0

while True:
    n = int(input("Ingresa un numero: "))
    if n > 0:
        suma += n
        divisor += 1
        promedio = suma / divisor  
    elif n < 0:
        suma2 += n
        divisor2 += 1
        promedio2 = suma2 / divisor2
    else:
        print("Numeros negativos:", divisor2,"Numeros positivos:", divisor)
        print("Promedio de negativos:", promedio2,"Promedio de positivos:",promedio)
        
