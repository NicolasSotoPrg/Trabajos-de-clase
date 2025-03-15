n = int(input("Ingresa la cantidad de numeros: "))
par = 0
suma = 0
promedio = 0
for i in range(n):
    m = int(input("Ingresa un numero: "))
    if m%2 == 0:
        suma = suma + m
        par = par +1
        promedio = suma / par
print("El promedio de los numeros pares que ingreso es: ",promedio)
