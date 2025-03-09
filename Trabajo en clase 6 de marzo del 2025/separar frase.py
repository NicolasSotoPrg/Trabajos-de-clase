frase = input("ingrese la frase ")
f = len(frase)
separar = ""
for i in range(f): 
    if frase[i] == " ":
      print(separar)
      separar = ""
    else:
     separar = separar+frase[i]
print(separar)      
