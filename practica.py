from ayuda import Matriz
nombre=input(f"Dime el nombre:\n")
continuar=True
while continuar:
    filas=int(input(f"Ingresa el numero de filas:\n"))
    columnas=int(input(f"ingresa el numero de columnas:\n"))
    if filas==columnas and filas==len(nombre):
        continuar=False
    else:
        print(f"Vuelve a ingresar los valores deben tener la misma longitud")
matriz=[]
for nfilas in range(filas):
    matriz.append([])
    for ncolumnas in range(columnas):
        if nfilas+ncolumnas==filas-1:
            matriz[nfilas].append(nombre[nfilas])
        else:
            matriz[nfilas].append(0)
print(Matriz(matriz))