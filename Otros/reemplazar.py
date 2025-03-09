entrada = input()
letra = input()
n = len(entrada)
salida = ""
for i in range(0, n - 1 + 1, 1):
    if entrada[i] == letra:
        salida = salida + "&"
    else:
        salida = salida + entrada[i]
print(salida)
