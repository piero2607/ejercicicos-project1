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

def hayMinacerca(coordJugador,coordsMina):
    xjugador,yjugador=coordJugador
    xmina,ymina=coordsMina
    diferencix=abs(xjugador-xmina)
    diferenciy=abs(yjugador-ymina)
    if diferencix<=1 and diferenciy<=1:
        if coordJugador!=coordsMina:
            return True
    return False

def cavar(m, m2,coordMina):
    print("Introduce las coordenadas donde quieres cavar:\n")
    try:
        x = int(input("x (0-4): "))
        y = int(input("y (0-3): "))
        if not(0<=x<=4 and 0<=y<=3):
            raise ValueError("coordenadas fuera de rango permitido")
        coordjugador=(x,y)
        if m2[coordjugador[1]][coordjugador[0]]=="⛏️":
            print("Ya cavaste aqui intenta en otra posicion")
            return None
        m[coordjugador[1]][coordjugador[0]] == "⛏️"
        m2[coordjugador[1]][coordjugador[0]] == "⛏️"
        if hayMinacerca(coordjugador,coordsMina):
            print("💀 Sientes una vibración en el suelo! Hay una mina cerca")
        return coordjugador

    except ValueError as e:
        print(e)
        return None


mapa = [["  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  "]]
mapaVacio = copy.deepcopy(mapa)
dibujarMapa(mapaVacio)
coordsMina, coordsTesoro = generarItems(mapa)
fin = False
print(f"cordenada de la mina {coordsMina}")
print(f"cordenadas del tesoro {coordsTesoro}")

while not fin:
    cordCavar = cavar(mapaVacio, mapa,coordsMina)
    if cordCavar is None:
        continue
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