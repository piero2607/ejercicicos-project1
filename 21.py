import random as r
palos=["espadas","copas","oros","bastos"]
numeros=[1,2,3,4,5,6,7,10,11]
figuras=["caballo","sota","oro"]
barajas=[]

def llenar_baraja():
    for numero in numeros :
        for palo in palos:
            barajas.append((numero,palo))
llenar_baraja()
print(barajas)
def carta():
    palo=r.choice(palos)
    numero=r.choice(numeros)
    return (numero,palo)
def valores(c):
    numero,palo=c
    if numero==10:
        nombre=r.choice(figuras)
    elif numero==1 or numero==11:
        nombre="as"
    else:
        nombre=str(numero)
    return f"{nombre}  de {palo}"
c=carta()
def repartir(jugador, casa, n=1):
    for _ in range(n):
        jugador.append(carta())
        casa.append(carta())
jugador = []
casa = []
repartir(jugador, casa, n=2)

print("Cartas del jugador:")
for c in jugador:
    print(valores(c))

print("\nCartas de la casa:")
for c in casa:
    print(valores(c))
