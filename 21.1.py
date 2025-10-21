import random as r
palos=["espadas","copas","oros","bastos"]
numeros=[1,2,3,4,5,6,7,8,9,10]
figuras=["caballo","sota","rey"]
barajas=[]

def llenar_baraja():
    for numero in numeros :
        if numero==8 or numero==9 or numero==10:
            for palo in palos:
                barajas.append((figuras[numero-8], palo))
        else:
            for palo in palos:
                barajas.append((numero,palo))
llenar_baraja()
print(barajas)
def valores(c):
    numero,palo=c
    if numero in figuras:
        numero=10
    if numero == 1:
        respuesta=int(input("el valo es un as quieres un (1-11)"))
        if respuesta==1:
            numero=1
        else:
            numero==11
    return f"{numero}  de {palo}"


def repartir(jugador, casa, n):
    for _ in range(n):
        jugador.append(carta())
        casa.append(carta())
jugador = []
casa = []
repartir(jugador, casa, 2)