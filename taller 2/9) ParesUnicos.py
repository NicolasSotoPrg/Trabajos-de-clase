def pares(lista, suma_objetivo):
    pares_encontrados = []

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):  
            #Empezamos en i + 1 para evitar repeticiones
            if lista[i] + lista[j] == suma_objetivo:
                #Sorted nos ayuda a ordenar el par para asegurar que (a, b) y (b, a) se traten igual
                par = sorted([lista[i], lista[j]])
                # Verificamos si el par ya fue agregado
                if par not in pares_encontrados:
                    print(par[0], par[1])
                    pares_encontrados.append(par)  
                    # Agregamos el par a la lista

def entrada():
    listanumeros = input("Ingresa una lista de números enteros separados por espacios: ")
    lista = list(map(int, listanumeros.split()))  # Convertimos la cadena en una lista de enteros

    # Pedir al usuario la suma objetivo
    suma_objetivo = int(input("Ingresa la suma objetivo: "))

    return lista, suma_objetivo

lista, suma_objetivo = entrada()
pares(lista, suma_objetivo)
