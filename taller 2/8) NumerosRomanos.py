nromanos = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),(90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I")]
#La lista se compone de simbolos de los cuales se derivan otros numero es importante el orden, ya que en el sistema romano primero se usan los valores mas grandes
#y se va restando de mayor a menor

def convercion(numero):
    resultado = ""
    for valor, simbolo in nromanos:
        #analizamos el numero ingresado en la lista, donde valor es el numero entero, y simbolo su correspondiente simbolo griego
        while numero >= valor:
            #si el numero ingresado es mayor a un valor, agregamos a "resultado" el simbolo
            resultado += simbolo
            #le restamos el valor al numero para que nos vaya dando el simbolo de los valores mas pequeños, por ejemplo
            #12 es mayor que 10 el cual tiene asignado el simbolo X,12 - 10 nos da 2,pero 2 es mayor a 1, entonces se imrime el simbolo I
            #pero 1 = 1 entonces se vuelve a imprimir I,el ciclo acaba al restar 1 - 1, lo cual es 0
            numero -= valor
    return resultado


while True:
    numero = int(input("Introduce un número entero positivo (0 para terminar): "))
    
    if numero == 0:
        #si el valor ingresado es 0 se cierra el while
        break
    
    if numero < 0:
        #No existen los numeros romanos negativos
        print("Por favor, ingresa un número positivo.")
        continue
    
    #si no hay algun error se llama la funcion 
    romano = convercion(numero)
    print(f"El número {numero} en romano es: {romano}")
