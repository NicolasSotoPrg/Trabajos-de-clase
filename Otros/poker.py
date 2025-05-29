import random

# Palos y rangos
palos = ['♠', '♥', '♦', '♣']
rangos = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def crear_baraja():
    baraja = []
    for palo in palos:
        for rango in rangos:
            baraja.append([rango, palo])
    random.shuffle(baraja)
    return baraja

def repartir(baraja, num_cartas):
    mano = []
    for _ in range(num_cartas):
        mano.append(baraja.pop())
    return mano

def mostrar_mano(mano):
    return " ".join([carta[0] + carta[1] for carta in mano])

def valor_rango(rango):
    return valores[rangos.index(rango)]

def contar_repetidos(mano):
    contador = []
    for carta in mano:
        existe = False
        for i in range(len(contador)):
            if contador[i][0] == carta[0]:
                contador[i][1] += 1
                existe = True
        if not existe:
            contador.append([carta[0], 1])
    return contador

def es_color(mano):
    primer_palo = mano[0][1]
    for carta in mano:
        if carta[1] != primer_palo:
            return False
    return True

def es_escalera(valores_ordenados):
    for i in range(len(valores_ordenados) - 1):
        if valores_ordenados[i] - 1 != valores_ordenados[i + 1]:
            return False
    return True

def evaluar_mano(mano):
    valores_mano = [valor_rango(carta[0]) for carta in mano]
    valores_mano.sort(reverse=True)
    repes = contar_repetidos(mano)
    repes.sort(key=lambda x: (x[1], valor_rango(x[0])), reverse=True)

    if len(repes) == 1 and repes[0][1] == 5:
        return [9, valor_rango(repes[0][0])]  # Repóker

    if repes[0][1] == 4:
        return [7, valor_rango(repes[0][0])]  # Póker

    if len(repes) == 2 and repes[0][1] == 3 and repes[1][1] == 2:
        return [6, valor_rango(repes[0][0]), valor_rango(repes[1][0])]  # Full

    if es_color(mano):
        return [5, valores_mano]  # Color

    if es_escalera(valores_mano):
        return [4, valores_mano[0]]  # Escalera

    if repes[0][1] == 3:
        return [3, valor_rango(repes[0][0])]  # Trío

    if len(repes) >= 2 and repes[0][1] == 2 and repes[1][1] == 2:
        return [2, valor_rango(repes[0][0]), valor_rango(repes[1][0])]  # Doble pareja

    if repes[0][1] == 2:
        return [1, valor_rango(repes[0][0])]  # Pareja

    return [0, valores_mano]  # Carta alta

def comparar_manos(mano1, mano2):
    eval1 = evaluar_mano(mano1)
    eval2 = evaluar_mano(mano2)
    if eval1 > eval2:
        return 1
    elif eval2 > eval1:
        return -1
    else:
        return 0

def ronda_apuestas(nombres, fichas, activos):
    print("\n--- Ronda de Apuestas ---")
    apuestas = [0 for _ in nombres]
    pozo = 0

    for i in range(len(nombres)):
        if not activos[i]:
            continue
        print(f"\n{nombres[i]}, tienes {fichas[i]} fichas.")
        accion = input("¿(a)postar, (p)asar o (r)etirarte?: ").lower()
        if accion == 'r':
            activos[i] = False
            print(nombres[i], "se ha retirado.")
        elif accion == 'a':
            try:
                cantidad = int(input("¿Cuánto quieres apostar?: "))
            except:
                cantidad = 0
            if cantidad > fichas[i]:
                cantidad = fichas[i]
            fichas[i] -= cantidad
            apuestas[i] += cantidad
            pozo += cantidad
            print(nombres[i], "apostó", cantidad)
        elif accion == 'p':
            print(nombres[i], "pasó.")
        else:
            print("Opción no válida. Se considera que pasaste.")
    return pozo, activos

def mostrar_comunitarias(comunitarias, cuantas):
    print("\nCartas comunitarias:")
    for i in range(cuantas):
        print(comunitarias[i][0] + comunitarias[i][1], end=" ")
    print()

def juego():
    nombres = input("Nombres de jugadores separados por coma: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    fichas = [1000 for _ in nombres]
    dealer = 0

    while all(f > 0 for f in fichas):
        print("\n=== Nueva Mano ===")
        baraja = crear_baraja()
        manos = []
        activos = [True for _ in nombres]

        for _ in nombres:
            manos.append(repartir(baraja, 2))

        comunitarias = repartir(baraja, 5)
        cartas_mostradas = 0
        pozo_total = 0

        # Mostrar cartas personales una por una
        print("\n--- Cartas Iniciales ---")
        for i in range(len(nombres)):
            input(f"\nTurno de {nombres[i]}. Presiona Enter para ver tus cartas.")
            print(f"Tus cartas: {mostrar_mano(manos[i])}")
            input("Presiona Enter para ocultar tus cartas.")
            print("\n" * 50)

        # Fase 1: Flop
        cartas_mostradas += 3
        mostrar_comunitarias(comunitarias, cartas_mostradas)
        pozo, activos = ronda_apuestas(nombres, fichas, activos)
        pozo_total += pozo

        # Fase 2: Turn
        vivos = [i for i in range(len(nombres)) if activos[i]]
        if len(vivos) > 1:
            cartas_mostradas += 1
            mostrar_comunitarias(comunitarias, cartas_mostradas)
            pozo, activos = ronda_apuestas(nombres, fichas, activos)
            pozo_total += pozo

        # Fase 3: River
        vivos = [i for i in range(len(nombres)) if activos[i]]
        if len(vivos) > 1:
            cartas_mostradas += 1
            mostrar_comunitarias(comunitarias, cartas_mostradas)
            pozo, activos = ronda_apuestas(nombres, fichas, activos)
            pozo_total += pozo

        # Mostrar ganador
        vivos = [i for i in range(len(nombres)) if activos[i]]
        if len(vivos) == 1:
            ganador = vivos[0]
            print(f"\n{nombres[ganador]} gana el pozo porque los demás se retiraron.")
        else:
            mejor = manos[vivos[0]] + comunitarias
            ganador = vivos[0]
            print("\n--- Mostrar manos ---")
            for i in vivos:
                actual = manos[i] + comunitarias
                print(f"{nombres[i]} tiene: {mostrar_mano(manos[i])}")
                if comparar_manos(actual, mejor) > 0:
                    mejor = actual
                    ganador = i
            print(f"\n{nombres[ganador]} gana el pozo con la mejor mano.")

        fichas[ganador] += pozo_total
        dealer = (dealer + 1) % len(nombres)
        input("Presiona Enter para continuar...")

juego()


