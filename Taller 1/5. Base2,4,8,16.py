n = int(input("Ingrese un numero: "))
b = int(input("ingrese una base 2,4,8 o 16: "))
letra =  ["A","B","C","D","F","E"]
numero = ["10","11","12","13","14","15"]
cv = ""

if b == 2 or 4 or 8 or 16:
    while n > 0:
        r = str(n % b)
        if r in numero:
          Posicion = numero.index(r)
          Posicion2 = letra[Posicion]
          cv = Posicion2 + cv
          n = n//b
        else:
          cv = r + cv
          n = n//b
    print("La conversion es: ",cv)
