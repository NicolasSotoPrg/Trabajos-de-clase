n=int(input("ingrese un numero "))
b=int(input("ingrese una base entre 2 y 10 "))
residuo=""
conversion=""
if b<10:
    if b>1:
        while n>0:
            residuo=str(n%b)
            conversion= residuo + conversion
            n=n//b
        print(conversion)         
    else:
        print("base no permitida,ingrese una entre 2 y 10")
else:
    print("base no permitida,ingrese una entre 2 y 10")  
        