palabras = input("Ingrese la palabra que desee pasar a pgilatin: ")
palabras = palabras.lower()
palabras = palabras.split(" ")
vocales = ["a","e","i","o","u"]
piglatin = ""

for palabra in palabras:
    if palabra[0] in vocales:
        piglatin += palabra + "yay "
    else:
        comienzo = 0
        for letra in list(palabra):
            if letra in vocales:
                break
            else:
                if letra is "y":
                    break
                else:
                    comienzo +=1
        piglatin += palabra[comienzo:] + palabra[:comienzo] + "ay "
print(piglatin)
