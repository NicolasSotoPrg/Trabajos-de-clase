palabra = input("Ingresa una palabra: ")

#Primero eliminamos las letras que se repiten
palabra2 = []
for i in palabra:
    #Creamos una lista sin caracteres, cada i es una letra, si esa letra no esta en la lista, se agrega, si esta significa que esa letra se repite, por ende, no se agrega
    if i not in palabra2:
        palabra2.append(i)
#Imprimimos los caracteres sin que se repitan para saber que cantidad se puede tomar para las permutaciones
print("Caracteres usables:", palabra2)

caracteres = int(input("Ingresa la cantidad de caracteres que se usaran en la permutacion: "))

#Revisamos que la cantidad de caracteres elegidos no supere la cantidad de caracteres que tiene la lista
if caracteres > len(palabra2):
    print("La cantidad supera los caracteres")
else:
    def permutaciones(lista, actual):
        #Si la cantidad de caracteres ejegida es la misma que tiene la lista, los volvemos a unir
        if len(actual) == caracteres:
            print(''.join(actual))  #Con .join unimos subcanes de una lista para convertirlas en una cadena,
            #Ponemos un return para que la funcion vuelva y continue con las combinaciones
            return
        for i in range(len(lista)):
            #Se toma uno de los elemetos y se elimina
            siguiente = lista[i]
            #Con esto vamos a tomar todos los caracteres que estan antes y despues, sin tomar el caracter i
            restantes = lista[:i] + lista[i+1:]
            permutaciones(restantes, actual + [siguiente])
            #se devulvelve restantes que es la nueva lista disponibeles y actual + [siguiente] que es la nueva lista que sale con los otros caracteres
    #Se llama la funcion con la lista de caractes ingresada y una lista vacia de donde saldran las nuevas permutaciones
    permutaciones(palabra2, [])
