def polinomio(coeficientes, x):
    #Calculamos el valor del polinomio para un valor x 
    resultado = 0
    # El grado es la posición del primer coeficiente, ques es uno menos que la cantidad de coeficientes
    grado = len(coeficientes) - 1  
    for i in range(len(coeficientes)):
        #Recorremos cada coeficiente, se calcula el exponente
        coef = coeficientes[i]
        exponente = grado - i
        #se evalua el polinomio, elevando el termino al exponente y multiplicandolo por el coeficiente
        #la suma es el valor del polinomio en x
        resultado += coef * (x ** exponente)
    return resultado
def area(coeficientes, n):
    #Calculamos el area en base a las sumas de riemann
    cain = 0
    for i in range(n):
        x = i / n
        #Dividimos el intervalo  [0, 1] en n partes
        #evaluamos la funcion en ese punto x
        funcion = polinomio(coeficientes, x)
        # Recortar el valor de f(x) dentro del rango [0, 1]
        if funcion < 0:
            #Si el valor de la funcion es negativa, no hay area
            funcion = 0
        elif funcion > 1:
            #Si es mayor que 1, se toma como 1
            funcion = 1   
        #calulamos el area del rectangulo, ancho = 1/n y alto = funcion, esto se suma
        cain += funcion / n  
    return cain
def reparto(coeficientes, n):
    #calculamos el area de cain
    area_cain = area(coeficientes, n)
    #comparar con la mitad de la hectárea
    diferencia = abs(area_cain - 0.5)  
    if diferencia <= 0.001:
        return "JUSTO"
    elif area_cain > 0.5:
        return "CAIN"
    else:
        return "ABEL"
def entradas(): 
    while True:
        grado = int(input("Ingresa el grado del polinomio (entre 0 y 19): ").strip())
        if grado == 20:
            #en el momento qye se ingrse un polinomio de grado 20 se termina el while
            break
        #Leemos los coeficientes como texto y los pasamos a enteros
        entrada = input("Ingresa los coeficientes del polinomio (de mayor a menor grado): ").strip().split()
        coeficientes = []
        for valor in entrada:
            #Esos coeficientes los pasamos a una lista
            coeficientes.append(int(valor))
        n = int(input("Ingresa la cantidad de rectángulos para hacer la suma: ").strip())
        #Evaluamos en la funcion
        resultado = reparto(coeficientes, n)
        print(resultado)
#Ejecutamos
entradas()
