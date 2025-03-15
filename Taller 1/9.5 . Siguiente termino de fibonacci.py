n = int(input("Ingrese un numero: "))
penultimo= 0
ultimo = 1
suma = 0
while suma <= n:
    suma = penultimo + ultimo
    penultimo = ultimo
    ultimo = suma
print(ultimo)
