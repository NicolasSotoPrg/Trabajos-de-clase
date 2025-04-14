import string 
#Esta libreria genera una lista con el abecedario INGLES 
#(De esto me di cuenta ya al final del programa), lo cual es un problema ya que en el ingles no existe la ñ por lo que el programa no la codifica
#ademas algunas letras las mueve una posicion mas.
print("1) Codificar")
print("2) Decodificar")
opcion = str(input("Ingrese la opcion a realizar: "))
#Menu para elegir entre codificar o decodificar la frase
abc = string.ascii_lowercase
#string.ascii es la libreria con el abecedario, la parte de _lowercase hace que la lista solo sea el abecedario en minusculas
def palabrapar(letra): #Esta funcion lo que hace es reemplazar las letras, de las palabras en posiciones pares
    #primero verificamos que el caracter ingresado sea una de las letras del abecedario
    if letra in abc:
        #Si se cumple, usamos .index para saber la posicion de esa letra en el abecedario y a ese numero le sumamos 3 que es el numero de posiciones 
        #que vamos a correr la letra, ejemplo con a, en la lista su indice es 0 al sumarle tres nos daria que ahora el indice es 3, que es la ubicacion de la letra d
        posicion = abc.index(letra) + 3
        if posicion >= 26:
            #Este if soluciona el problema con w,x,y y z, que al sumarles 3 o 4 en caso de las palabras impares, su posicion se pasa del numero de letras que hay en el abecedario
            #si la posicion se pasa de 26 (que es el numero de letras que hay en el abecedario ingles), se le resta 26,para que el cambio de posiciones se reinicie,
            #ejemplo con x, esta en la posicion 24 ,si se le suma 3, da 27 pero si se le resta 27 el indice daria 0,entoces se imprime a
            posicion2 = posicion - 26
            posicion3 = str(abc[posicion2])
            #la posicion3 es la letra ya trasladada
        else:
            posicion3 = str(abc[posicion])
            #En los demas casos que no son w,x,y o z simplemente se imprime la letra que esta en el nuevo indice
    else: 
        posicion3 = letra
        #En el caso que el caracter sea un punto, coma, punto y coma,etc. se imprimira tal cual
    return posicion3   
def palabraimpar(letra): #Esta funcion es exactamente la anterior pero se usa en las palabras impares, donde las letras se deben mover 4 posiciones
    if letra in abc:
        posicion = abc.index(letra) + 4
        if posicion >= 26:
            posicion2 = posicion - 26
            posicion3 = str(abc[posicion2])
        else:
            posicion3 = str(abc[posicion])
    else: 
        posicion3 = letra
    return posicion3  
def codificado(a):#Como tal aqui es donde se codifica la frase
    frase = a.lower()
    #a es la frase que se ingresa, usamos .lower para que las letras esten en minusculas y y facilitar la codificacion
    sp = frase.split(" ")
    #sp es una lista, la cual sale de .split el cual en base a una cadena crea subcadenas cuando se cumple una condicion, en este caso la condicion son los espacios
    #cuando se detecta un espacion se genera la subcadena, con esto separamos las palabras de las frase
    npalabras = len(sp)
    #con esto hacemos un conteo de las palabras que hay
    palabracifrada = ""
    cifradocesar = ""

    for i in range(npalabras):
        palabra = sp[i]
        #Para la parte de saber si una palabra es par o impar tambian usaremos los indices, cada i es una palabra y toma valores desde 0 
        #por ende con este i podemos saber si el residuo da o no da 0 y con esto sabemos si la palabra esta en una posicion par o impar
        r = i%2
        if r == 0:
            traduccionp = ""
            for letra in palabra:
                #se recorre cada letra que hay en la palabra, esta letra ingresa a la funcion palabrapar que la mueve 3 posiciones
                traduccionp += palabrapar(letra)
                #y se cambia a la variable palabracifrada para poder unilar con las palabras que estebn en posiciones impares
                palabracifrada = traduccionp
        else:
            #si su residuo no es 0 significa que es impar, y se hace lo mismo que en el caso de los pares pero usando la funcion de palabraimpar
            traduccioni = ""
            for letra in palabra:
                traduccioni += palabraimpar(letra)
                palabracifrada = traduccioni 
        #por ultimo las unimos en una sola cadena que seria cifradocesar y le agregamos un espacio ya que al usar .split esa fue nuestra condicion para separarlas
        #si se separo significa que en la frase original al frente de esa palabra si o si iba un espacio
        cifradocesar += palabracifrada + " "
    return cifradocesar
def decodificadorpar(letra):#En esta funcion se hace lo mismo que en la funcion palabrapar pero en vez de sumarle 3 al indice, se le restan, para volver a la ubicacion original de la letra
    if letra in abc:
        posicion = abc.index(letra) - 3
        if posicion >= 26:
            posicion2 = posicion - 26
            posicion3 = str(abc[posicion2])
        else:
            posicion3 = str(abc[posicion])
    else: 
        posicion3 = letra
    return posicion3  
def decodificadorimpar(letra):#Se hace lo mismo que en la funcion decodificadorimpar pero en vez de restarle 3 se le resta 4
    if letra in abc:
        posicion = abc.index(letra) - 4
        if posicion >= 26:
            posicion2 = posicion - 26
            posicion3 = str(abc[posicion2])
        else:
            posicion3 = str(abc[posicion])
    else: 
        posicion3 = letra
    return posicion3  
def decodificado(a):#Se hace lo mismo que en la funcion codificado pero cambiando internamente las funciones palabrapar y palabraimpar por decodificadorpar y decodificadorimpar
    frase = a.lower()
    sp = frase.split(" ")
    npalabras = len(sp)
    palabracifrada = ""
    cifradocesar = ""

    for i in range(npalabras):
        palabra = sp[i]
        r = i%2
        if r == 0:
            traduccionp = ""
            for letra in palabra:
                traduccionp += decodificadorpar(letra)
            palabracifrada = traduccionp
        else:
            traduccioni = ""
            for letra in palabra:
                traduccioni += decodificadorimpar(letra)
            palabracifrada = traduccioni 
        cifradocesar += palabracifrada + " "
    return cifradocesar

#Estas son las respuestas a las opciones del menu
if opcion == "1":
    #si la respuesta es "1" quiere codificar, se le pide la frase, y esta se manda a la funcion codificado
    a = str(input("Ingresa la frase a codificar: "))
    print(codificado(a))
elif opcion == "2":
    #si la respuesta es "2" quiere descodificar, se le pide la frase, y esta se manda a la funcion descodificado
    deco = str(input("Ingresa la frase a decodificar: "))
    print(decodificado(deco))
