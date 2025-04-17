#Para el codigo vamos a tener en cuenta que un numero tiene cuadrado perfecto si al descomponerse en factores primos los exponentes de ellos son pares.
#Ejemplo el 8 se puede descomponer en 2*2*2 que seria lo mismo que 2^3, como dicho exponente es impar, tenemos que hacer que se vuelva par, este caso si se multiplica por 2
#El resultado seria 2^4, que seria 16 y el cuadrado perfecto de 16 es 4

def multiplocuadradoperfecto(n):
    #En esta parte vamos descomponer los numeros primos que hay en el numero
    factores = {}
    i = 2
    while i * i <= n:
        # Contar cuántas veces n es divisible por i
        contador = 0
        while n % i == 0:
            contador += 1
            n = n // i
        if contador % 2 != 0:
            factores[i] = 1  # Solo nos interesa si el exponente es impar, ya que es el que hace que no sea cuadrado perfecto
        i += 1
    # Si queda un factor primo mayor que la raíz
    if n > 1:
        factores[n] = 1
    # Multiplicar los primos con exponentes impares
    resultado = 1
    for primo in factores:
        resultado *= primo
    return resultado

# Leer el número de casos
casos = int(input("Ingresa la cantidad de numeros:"))
for _ in range(casos):
    numero = int(input("Ingresa un numero:"))
    print(f"Para que el numero se convierta en un numero con cuadrado perfecto se debe multiplicar por: {multiplocuadradoperfecto(numero)}")
