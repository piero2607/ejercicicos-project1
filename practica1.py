import random as r

from  ayuda import Matriz
matriz1=[]
for i in range(10):
    valores1=r.randint(0,100)
    matriz1.append(valores1)
matriz2=[]
for i in range(10):
    valores2=r.randint(0,100)
    matriz2.append(valores2)
suma=[]
for i in range(10):
    suma.append(matriz1[i]+matriz2[i])
print(suma)