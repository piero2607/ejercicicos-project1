from Imprimir import imprimirMatriz

matriz_magica=[
    [16,3,2,13],
    [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1]
]

imprimirMatriz(matriz_magica)
sumafilas=0
for i in range(len(matriz_magica)):
    sumafilas=sum(matriz_magica[i])
    print(f' la sumafila {i+1} = {sumafilas}')
for j in range(len(matriz_magica)):
    sumaColumna = 0
    for i in range(len(matriz_magica)):
        sumaColumna+=(matriz_magica[i][j])
    print(f'la suma Columna {j+1} = {sumaColumna}')
suma_diagonal_principal=0
for i in range(len(matriz_magica)):
    for j in range(len(matriz_magica)):
        if i==j:
            suma_diagonal_principal+=matriz_magica[i][j]
print(f'la suma de ladiagonal principal es: {suma_diagonal_principal}\n')
suma_diagonal_secundria=0
for i in range(len(matriz_magica)):
    for j in range(len(matriz_magica)):
        if i+j==len(matriz_magica)-1:
            suma_diagonal_secundria+=matriz_magica[i][j]
print(f"la suma de la diagonal secundaria es: {suma_diagonal_secundria}\n")
suma_magica=sum(matriz_magica[0])
if suma_magica == sumafilas and suma_magica == sumaColumna and \
   suma_magica == suma_diagonal_principal and suma_magica == suma_diagonal_secundria:
    print("✅ La matriz es mágica")
else:
    print("❌ La matriz NO es mágica")