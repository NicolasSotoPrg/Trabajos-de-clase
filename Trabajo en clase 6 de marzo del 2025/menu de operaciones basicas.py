
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a // b


while True:
    print("1) Realizar Suma")
    print("2) Realizar Resta")
    print("3) Realizar Multiplicacion")
    print("4) Realizar Division")
    print("5) Salir")


    opcion = input("Escribe el numero de la operacion a realizar: ")
    
    if opcion == "5":
        print("Gracias por usar el programa")
        break

    n1 = int(input("Ingresa el primer numero: "))
    n2 = int(input("Ingresa el segundo numero: "))
    if opcion == "1":
        print("Resultado = ",suma(n1, n2))
    elif opcion == "2":
        print("Resultado = ",resta(n1, n2))
    elif opcion == "3":
        print("Resultado = ",multiplicacion(n1, n2))
    elif opcion == "4":
        print("Resultado = ",division(n1, n2))
