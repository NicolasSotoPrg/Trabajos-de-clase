import random as rnd
X = []
Y = []
n = 2
smp = 0
smx = 0
smy = 0
mx2 = 0
smx2 = 0
for i in range(n):
    #Lo siguiente es para generar datos randoms para Y y X, X toma un intervalo de 150 a 210 (Altura de la persona)
    #y Y toma un intervalo de 40 a 300 (Peso de la persona)
    X.append(rnd.randint(150, 210))
    Y.append(rnd.randint(40, 300))
    #Basado en la formula, separamos los procesos, para despues unirlos
    #1)Hacemos la sumatoria de los valores que nos da al multiplicar x*y
    mp = X[i] * Y[i]
    smp += mp
    #2)Hacemos la sumatoria de todos los valores X y todos los valores Y
    smx += X[i]
    smy += Y[i]
    #3)Hacemos la sumatoria de cada valor de x elevado al cuadrado
    mx2 = X[i] ** 2
    smx2 += mx2
#4)Multiplicamos las sumatorias de los valores de x y de y
mps = smx * smy
#5)Elevamos al cuadrado la sumatoria de los vamores de x
smx3 = smx ** 2
#6)Reemplazamos en la formula, para hayar la PENDIENTE de la recta
m = (n*smp - mps) / (n*smx2 - smx3)
print(X)
print(Y)
print(m)
