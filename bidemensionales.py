from Imprimir import imprimirMatriz

continuar=False
while not continuar:
    filas=int(input('Dime el numero de filas:\n'))
    columnas=int(input('Dime  el numero de columnas:\n'))
    if filas==columnas:
        continuar=True
    else:
        print('las filas y columnas deben ser igual para que sea cuadrada.....')
matriz=[]
for fila in range(filas):
    matriz.append([])
    for columna in range(columnas):
        if fila+columna==filas-1:
            matriz[fila].append(1)
        else:
            matriz[fila].append(0)

imprimirMatriz(matriz)