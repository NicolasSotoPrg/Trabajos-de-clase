n = str(input("Ingrese un numero: "))
m = len(n)
ps = ""
suma = ""
for i in range(m):
    numero = int(n[i])
    if numero == 9:
        ps = "0"
    else: 
        ps = str(numero + 1)
    suma += ps
print("El resultado es: ",suma)
