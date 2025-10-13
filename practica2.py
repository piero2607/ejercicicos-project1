import random

from ayuda import Matriz
continuar=True
while continuar:
    filas = int(input("Dime el numero de filas:\n"))
    columnas = int(input("Dime el numero de columnas:\n"))
    if filas==columnas:
        continuar=False
    else:
        print("filas y columnas deben ser iguales")
matriz=[]
pares=0
impares=0
for nfilas in range(filas):
    fila=[]
    for ncolumnas in range(columnas):
        numeros=random.randint(0,100)
        fila.append(numeros)
        if numeros%2==0:
            pares+=1
        else:
            impares+=1
    matriz.append(fila)
print(Matriz(matriz))
print(f"Numero de pares {pares}")
print(f"Numero de impares {impares}")

