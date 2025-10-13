import copy
import random as r


def dibujarMapa(m):
    x = 3
    for i in range(len(m) - 1, -1, -1):
        print(f"{x}: {m[i]}")
        x -= 1
    print("     0,     1,    ,2     ,3     4")


def generarItems(m):
    mina = "💣"
    tesoro =  "💰"
    coordsMina = (r.randint(0, 4), r.randint(0, 3))
    coordsTesoro = coordsMina
    while coordsMina == coordsTesoro:
        coordsTesoro = (r.randint(0, 4), r.randint(0, 3))
    m[coordsMina[1]][coordsMina[0]] = mina
    m[coordsTesoro[1]][coordsTesoro[0]] = tesoro
    return coordsMina, coordsTesoro


def cavar(m, m2):
    print("Introduce las coordenadas donde quieres cavar:\n")
    coords = (int(input("x: ")), int(input("y: ")))

    m[coords[1]][coords[0]] = "⛏️"
    m2[coords[1]][coords[0]] = "⛏️"


    return coords


mapa = [["  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  "]]
mapaVacio = copy.deepcopy(mapa)
dibujarMapa(mapaVacio)
coordsMina, coordsTesoro = generarItems(mapa)
fin = False
print(f"cordenada de la mina {coordsMina}")
print(f"cordenadas del tesoro {coordsTesoro}")

while not fin:
    cordCavar = cavar(mapaVacio, mapa)
    if cordCavar == coordsTesoro:
        print("has ganado.")
        dibujarMapa(mapa)
        fin = True
    elif cordCavar == coordsMina:
        print("Has perdido!")
        dibujarMapa(mapa)
        fin = True
    else:
        dibujarMapa(mapaVacio)