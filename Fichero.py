datos={}
with open("datos.txt","r") as r:
    for linea in r:
        nombre,edad=linea.strip().split(":")
        datos[nombre]=int(edad)
print(datos)
nombre=input("por favor introduce un nombre para verificar si esta en la lista:\n")
if nombre in datos:
    print(f"{nombre} tiene {datos[nombre]} años")
else:
    edad=int(input(f"{nombre} no esta en la lista introdeuce su edad:\n"))
    datos[nombre]=edad
with open("datos_actualizados.txt","w") as f:
    for nombre,edad in datos.items():
        f.write(f"{nombre}:{edad}:\n")