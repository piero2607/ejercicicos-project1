import random as r

from Imprimir import imprimirMatriz

matriz=[]
for i in range(4):
    matriz.append([])
    for j in range(4):
        n_aleatorio = r.randint(0, 9)
        matriz[i].append(n_aleatorio)

imprimirMatriz(matriz)
sumafilas=0

for i in range(len(matriz)):
    sumafilas=sum(matriz[i])
    print(f' la sumafila {i+1} = {sumafilas}')
for j in range(len(matriz)):
    sumaColumna = 0
    for i in range(len(matriz)):
        sumaColumna+=(matriz[i][j])
    print(f'la suma Columna {j+1} = {sumaColumna}')


