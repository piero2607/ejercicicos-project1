from ayuda import Matriz
def fiboonacci(n):
    a, b = 0, 1
    fibo = []
    for _ in range(n):
        fibo.append(a)
        a, b = b, a + b
    return fibo

continuar=True
while(continuar):
    filas=int(input("ingresa el numero de filas:\n"))
    columnas=int(input("introduce el numero de columnas:\n"))
    if 5<=filas<=35 and 5<=columnas<=35:
        continuar=False
    else:
        print("vuelve a introducir los valores entre(5-35):\n")
fibo=fiboonacci(filas)
matriz=[]
for nfilas in range(filas):
    matriz.append([])
    for ncolumnas in range(columnas):
        if nfilas+ncolumnas==filas-1:
         matriz[nfilas].append(fibo[nfilas])
        else:
            matriz[nfilas].append(0)
print(Matriz(matriz))